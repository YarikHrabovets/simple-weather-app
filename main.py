import socket

import eel

from pyowm import OWM
from pyowm.utils.config import get_default_config
import pyowm.commons.exceptions

import geocoder
import pytz
from timezonefinder import TimezoneFinder
from datetime import datetime

from translate import Translator

from user_json import UserHistory

translator = Translator(from_lang='russian', to_lang='english')
user = UserHistory('history_list.json')

geo = str(geocoder.ip('me')[:1]).replace('[', '').replace(']', '')
location = geo.split(',')[0]

config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM('340ce2e89549964b40571041946d4ae9') # free api token for everyone 
mgr = owm.weather_manager()
geo_mgr = owm.geocoding_manager()
obj = TimezoneFinder()
observation = mgr.weather_at_place(f'{location}')
weather = observation.weather


@eel.expose
def current_place() -> str:
    return location


@eel.expose
def current_city_time() -> list:
    coordinate = geo_mgr.geocode(location)[0]
    tz = obj.timezone_at(lat=coordinate.lat, lng=coordinate.lon)
    time_list = str(datetime.now(tz=pytz.timezone(tz)))[11:19].split(':')
    time_list = [int(i) for i in time_list]
    return time_list


@eel.expose
def current_weather() -> list:
    return [weather.temperature(eel.getTemperatureInfo()()), weather.wind()['speed'], weather.humidity,
            weather.detailed_status, weather.sunrise_time(timeformat='iso')[11:16], weather.sunset_time(timeformat='iso')[11:16],
            weather.clouds, weather.humidity, weather.visibility_distance
            ]


@eel.expose
def _dump(city: str):
    try:
        user.dump(city.capitalize(), translator.translate(city).capitalize(), str(datetime.now())[:19])
        eel.sleep(1.0)
    except RuntimeError:
        pass


@eel.expose
def _load() -> list:
    return user.load()


@eel.expose
def _remove(index: int):
    user.remove(index)


@eel.expose
def update(city: str):
    global location, observation, weather
    try:
        _city = translator.translate(city).capitalize()
        observation = mgr.weather_at_place(_city)
        weather = observation.weather
        location = _city
        eel.sleep(1.0)
    except pyowm.commons.exceptions.NotFoundError:
        eel.alert('Мы не смогли найти такой регион!', 'danger')
    except RuntimeError:
        eel.alert('Мы не смогли найти такой регион!', 'danger')
    else:
        return True


@eel.expose
def get_from_history(city: str):
    global location, observation, weather
    observation = mgr.weather_at_place(city)
    weather = observation.weather
    location = city


if __name__ == '__main__':
    eel.init('web')
    eel.start('html/index.html', size=(750, 600), host=socket.gethostbyname('localhost'), port=8080)
