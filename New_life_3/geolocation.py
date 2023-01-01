# import requires modules
from geopy.geocoders import Nominatim  # Подключаем библиотеку
from parsers.parser_coffee import coffee_address
from parsers.parser_location_address import *
locations_latitude_and_longitude = []
location_no_duplicates = []
locations_latitude_and_longitude_cinema = []
location_no_duplicates_cinema = []


# # address we need to locate
# loc = 'Gomel'
#
# # finding the location
# location = geocode(loc, provider="nominatim", user_agent='my_request')
# #
# point = location.geometry.iloc[0]
# print('Name: ' + loc)
# print('complete address: ' + location.address.iloc[0])
# print('longitude: {} '.format(point.x))
# print('latitude: {} '.format(point.y))
#
# geolocator = Nominatim(user_agent="Testess") #Указываем название приложения (так нужно, да)
# adress = str(input('Введите адрес: \n')) #Получаем интересующий нас адрес
# location = geolocator.geocode(adress) #Создаем переменную, которая состоит из нужного нам адреса
# print(location) #Выводим результат: адрес в полном виде
# print(location.latitude, location.longitude)
# # 52.4321132 31.0005449

geolocator = Nominatim(user_agent="Tester")  # Указываем название приложения (так нужно, да)
for i in coffee_address:
    location = geolocator.geocode(i, timeout=10)
    if location is None:
        locations_latitude_and_longitude.append(None)
    else:
        locations = location.latitude, location.longitude

        locations_latitude_and_longitude.append(locations)

location_no_duplicates = list(set(locations_latitude_and_longitude))
loc_geo = list(filter(None, location_no_duplicates))
print(loc_geo)

# Перевод в широту и долготу для кинотеатров
geolocator_cinema = Nominatim(user_agent="Cinema")  # Указываем название приложения (так нужно, да)
for i in loc_address_cinema:
    location_cinema = geolocator.geocode(i, timeout=10)
    if location_cinema is None:
        locations_latitude_and_longitude_cinema.append(None)
    else:
        locations_cinema = location_cinema.latitude, location_cinema.longitude

        locations_latitude_and_longitude_cinema.append(locations_cinema)

location_no_duplicates_cinema = list(set(locations_latitude_and_longitude_cinema))
loc_geo_cinema = list(filter(None, location_no_duplicates_cinema))
print(loc_geo_cinema)
