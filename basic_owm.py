import sys
import os
import locale
from datetime import datetime
import time
import requests, json
from pprint import pprint

#Set url
API_KEY = 'YOURKEYHERE'
LOCATION = 'Québec, CYQB'
LATITUDE = '46.790733'
LONGITUDE = '-71.388601'
UNITS = 'metric'
LANGUAGE = 'fr'

#url
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
url = BASE_URL + 'lat=' + LATITUDE + '&lon=' + LONGITUDE + '&units=' + UNITS +'&appid=' + API_KEY +'&lang=' + LANGUAGE

#Get data
response = requests.get(url)
data = response.json()

#Define             
temp = data['main']['temp']
wind_speed = data['wind']['speed']
wind_km = wind_speed * 3.6
wind_dir = data['wind']['deg']
latitude = data['coord']['lat']
longitude = data['coord']['lon']
description = data['weather'][0]['description']
#icon = data['weather'][0]['icon']
#icon_URL = 'https://openweathermap.org/img/wn/'+ icon +'@4x.png'
pressure = data['main']['pressure']
humidity = data['main']['humidity']
maxi = data['main']['temp_max']
mini = data['main']['temp_min']

#To do: convert wind degree to compass

# Set strings to be printed to screen
string_location = 'Présentement à ' + LOCATION
string_temp = format(temp, '.1f') + u'\N{DEGREE SIGN}C'
string_description = '  ' + description.title()
string_humidity = 'Humidité: ' + str(humidity) + '%'
string_maxi = "Maximum : " + format(maxi, '>.1f') + u'\N{DEGREE SIGN}C'
string_mini = "Minimum : " + format(mini, '>.1f') + u'\N{DEGREE SIGN}C'
string_wind = 'Vent: ' + format(wind_km, '.1f') + ' km/h'
string_wind_dir = '  ' + str(wind_dir) + u'\N{DEGREE SIGN}'

#Print
print (string_location)
print ((string_temp) + (string_description))
print ((string_wind) + (string_wind_dir))
print (string_humidity)
print ()
print (string_maxi)
print (string_mini)

