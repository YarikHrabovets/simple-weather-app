import json
from json.decoder import JSONDecodeError
from pathlib import Path


class UserHistory:
    def __init__(self, json_name):
        self.path = Path(json_name)

    def dump(self, city: str, city_translate: str, date: str):
        with open(self.path, 'r', encoding='utf-8') as file:
            try:
                data = file.read()
                data = json.loads(data)
            except JSONDecodeError:
                data = []

        unique = True
        for i in range(len(data)):
            if city in data[i][f'city_{i}']:
                unique = False
                break

        if unique:
            k = len(data)
            frame = {f'city_{k}': [city, city_translate], f'date_{k}': date}
            data.append(frame)

            with open(self.path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)

    def load(self) -> list:
        with open(self.path, 'r', encoding='utf-8') as file_:
            try:
                data = json.loads(file_.read())
            except JSONDecodeError:
                data = []
        return data

    def remove(self, index: int):
        with open(self.path, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
            except JSONDecodeError:
                data = []

            if len(data) > 0 and index <= len(data)-1:
                data.remove(data[index])
                data_copy = data.copy()
                for i, j in zip(data_copy, range(len(data_copy))):
                    k_copy, v_copy = list(i.keys()).copy(), list(i.values()).copy()
                    for k, v in zip(k_copy, v_copy):
                        del data[j][k]
                        data[j][k.replace(k[-1], str(j))] = v

                with open(self.path, 'w', encoding='utf-8') as file_:
                    json.dump(data, file_, indent=4)
