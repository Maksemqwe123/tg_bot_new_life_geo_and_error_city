# import requires modules
from geopy.geocoders import Nominatim  # Подключаем библиотеку
from parsers.parser_coffee import recond, coffee_address
locations_latitude_and_longitude = []
location_no_duplicates = []

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
# # # 52.4321132 31.0005449

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
# print(loc_geo)



