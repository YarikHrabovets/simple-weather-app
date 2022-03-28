async function getCurrentWeather() {
	const place = await eel.current_place()();
	const weather = await eel.current_weather()();

	document.getElementById("city").innerHTML = place;
	document.getElementById("status").innerHTML = `(${weather[3]})`;
	document.getElementById("temperature").innerHTML = `${Math.round(weather[0]['temp'])}°`;
	document.getElementById("min-temperature").innerHTML = `min: ${Math.round(weather[0]['temp_min'])}°`;
	document.getElementById("max-temperature").innerHTML = `max: ${Math.round(weather[0]['temp_max'])}°`;
	document.getElementById("wind-speed").innerHTML = `${Math.round(weather[1])} м/с`;
	document.getElementById("sunrise").innerHTML = weather[4];
	document.getElementById("sunset").innerHTML = weather[5];
	document.getElementById("clouds").innerHTML = `${weather[6]} %`;
	document.getElementById("humidity").innerHTML = `${weather[7]} %`;
	document.getElementById("visibility-distance").innerHTML = `${weather[8]}(м)`;

	document.getElementById("linear").style.visibility = "hidden";
}
