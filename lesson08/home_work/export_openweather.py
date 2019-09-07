""" OpenWeatherMap (экспорт)

Сделать скрипт, экспортирующий данные из базы данных погоды, 
созданной скриптом openweather.py. Экспорт происходит в формате CSV или JSON.

Скрипт запускается из командной строки и получает на входе:
    export_openweather.py --csv filename [<город>]
    export_openweather.py --json filename [<город>]
    export_openweather.py --html filename [<город>]
    
При выгрузке в html можно по коду погоды (weather.id) подтянуть 
соответствующие картинки отсюда:  http://openweathermap.org/weather-conditions

Экспорт происходит в файл filename.

Опционально можно задать в командной строке город. В этом случае 
экспортируются только данные по указанному городу. Если города нет в базе -
выводится соответствующее сообщение.

"""
# !/usr/bin/env python3

import csv
import json
import requests
import os
import datetime

url = "https://community-open-weather-map.p.rapidapi.com/weather"
city = input('Укажите город, на английском \n')
dir_path = os.path.join(os.getcwd(), 'Data')
try:
    os.mkdir(dir_path)
except FileExistsError:
    pass
os.chdir(dir_path)
querystring = {"id": "2172797", "units": "metric", "mode": "xml, html", "q": city}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "d806b9b004msh56975176a9668a0p1710bfjsne6465b650fc1"
}

var = {'coord': {'lon': 37.62, 'lat': 55.75},
       'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}], 'base': 'stations',
       'main': {'temp': 21.43, 'pressure': 1023, 'humidity': 60, 'temp_min': 21, 'temp_max': 22}, 'visibility': 10000,
       'wind': {'speed': 3, 'deg': 320}, 'clouds': {'all': 40}, 'dt': 1567848245,
       'sys': {'type': 1, 'id': 9029, 'message': 0.0079, 'country': 'RU', 'sunrise': 1567824305, 'sunset': 1567872645},
       'timezone': 10800, 'id': 524901, 'name': 'Moscow', 'cod': 200}

response = requests.request("GET", url, headers=headers, params=querystring)
answer = response.json()

my_city = answer['weather'][0]['main'] + ' ' + answer['weather'][0]['description'] + ' ' + str(answer['main']['temp'])
now = datetime.datetime.today()
data = open(city, 'w')
data.write(now.isoformat(sep='T') + '\n')
data.write(my_city)
