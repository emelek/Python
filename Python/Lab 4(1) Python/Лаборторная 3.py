from pyowm import OWM

API_key = 'c5fed2aabc1ab49b5b1b78ecfb303452'
owm = OWM(API_key)

city = input('Введите город: ')
observation = owm.weather_at_place(city + ',ru')
weather = observation.get_weather()
location = observation.get_location()

#форматируем выходные данные
press = round(dict.get(weather.get_pressure(),'press') * 0.75)
print (press)

tempSr = dict.get(weather.get_temperature('celsius'),'temp')
tempNo = dict.get(weather.get_temperature('celsius'),'temp_min')
tempDe = dict.get(weather.get_temperature('celsius'),'temp_max')

windVector = dict.get(weather.get_wind(),'deg')
if windVector >= 22.5:
    windDirection = 'северный'
elif windVector >= 67.5:
    windDirection = 'северо-восточный'
elif windVector >= 112.5:
    windDirection = 'восточный'
elif windVector >= 157.5:
    windDirection = 'юго-восточный'
elif windVector >= 202.5:
    windDirection = 'южный'
elif windVector >= 247.5:
    windDirection = 'юго-западный'
elif windVector >= 292.5:
    windDirection = 'западный'
elif windVector >= 337.5:
    windDirection = 'северо-западный'
else:
    windDirection = 'северный'

windSpeed = dict.get(weather.get_wind(),'speed')

if weather.get_clouds() >= 50:
    pasmurnost = 'пасмурная'
elif weather.get_clouds() >= 25:
    pasmurnost = 'c прояснениями'
else:
    pasmurnost = 'ясная'

message = 'Погода в городе ' + city + ' (' + location.get_country()+\
') на сегодня в ' + str(weather.get_reference_time('iso')) + ' ' + \
 pasmurnost + ', облачность составляет ' + str(weather.get_clouds()) + \
'%, давление ' + str(press) + ' температура воздуха ' + str(tempSr) + \
' градусов Цельсия, ночью ' + str(tempNo) + ' днём ' +str(tempDe) +\
 ' ветер ' + windDirection + ' скорость ' + str(windSpeed) + ' м/с.'

print(message)