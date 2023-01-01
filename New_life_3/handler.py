from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State

from New_life_3.parsers.parser_cinema import all_cinema
from weather_tg_bot import *  #!!!
from New_life_3.weatear import ru
from New_life_3.config import *
from buttons import *
import h3
import re
from geolocation import *
# from parsers.parser_pizza import list_pizza
from New_life_3.parsers.parser_kinogo import all_kinogo
from New_life_3.parsers.parser_litres import all_books
from New_life_3.parsers.cook_parser import all_cooks
from New_life_3.parsers.parser_restaurant_pizza import all_pizza
from New_life_3.parsers.parser_coffee import all_coffee
from sqlite import Database
from geopy.geocoders import Nominatim
import requests
import random
import aiofiles

db = Database('database.db')
number = random.randint(1, 20)

count_of_attempts = 1
metrix_1 = []
me = []
me_cinema = []
koi = []
users = {}


@dp.message_handler(commands='start')
async def start_message(message: types.Message):
    if message.chat.type == 'private':
        if not db.create_profile(message.from_user.id):
            db.edit_profile(message.from_user.id)
        await message.answer('Привет, я бот который подскажет как провести день, в связи с погодой',
                             reply_markup=user_kb)
        await message.answer('В каком городе ты хочешь узнать погоду?🌤')


@dp.message_handler(commands='sendall')
async def send_all(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == ADMIN_ID:
            text = message.text[9:]
            users_id = db.get_users()
            for row in users_id:
                try:
                    await bot.send_message(row[0], text)

                except:
                    db.set_active(row[0], 0)

            await bot.send_message(message.from_user.id, "Успешная рассылка")


@dp.message_handler(Text(equals=cities, ignore_case=True))
async def today(message: types.Message):
    p = message.text
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={OPEN_WEATHER_TOKEN}&units=metric&lang={ru}"
        )
        data = r.json()

        # if message.chat.type == 'private':
        #     db.city_user(message.text)

        # if not db.create_profile(p):
        #     db.edit_profile(None, p)

        # if str(message.from_user.id) not in users.keys():
        #     users[str(message.from_user.id)] = message.from_user.full_name
        #
        #     async with aiofiles.open('users_datas.txt', 'w+') as users_file:
        #         for ID, username in users.items():
        #             await users_file.write(f'ID: {ID} | Username: {username}, CITY: {p}')
                    # db.city_user(message.text)

        city = data["name"]
        cur_weather = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]
        wind = data["wind"]["speed"]

        await message.answer(f'В городе: {city} \nТемпература воздуха: {cur_weather} C \nОжидается: {weather_description}\n'
                             f'Скорость ветра: {wind} м/c', reply_markup=house_or_street)

        if cur_weather < 5 and cur_weather > -4:
            await message.answer('cегодня на улице немного холодно, возможно слякоть и гололёд,'
                                 'можно остаться дома или пойти на улицу')

        elif cur_weather < -4 and cur_weather > -8:
            await message.answer('сейчас на улице холодно, оденься потеплее, желательно ещё поесть перед выходом')

        elif cur_weather < -9 and cur_weather > -16:
            await message.answer('сейчас на улице довольно холодно, посоветую тебе остаться дома,'
                                 ' но если тебе не страшен холод, могу посоветовать куда можно сходить  ')

        elif cur_weather < -16:
            await message.answer('cейчас на улице очень холодно, останься лучше дома')

    except:
        await message.reply("Проверьте название города")


@dp.message_handler(Text(equals='Что можно поделать дома ?🏠', ignore_case=True))
async def leisure(message: types.Message):
    await message.answer('можно посмотреть/почитать фильм/книгу, но перед этим, я бы посоветовал заварить чая/кофе.\n'
                         'могу подсказать как легко и просто приготовить вкусный десерт,'
                         'так же проходит акция при заказе пиццы', reply_markup=help_assistant_house)


@dp.message_handler(Text(equals='Как можно провести время на улице ?🚶‍♂🚶‍♀', ignore_case=True))
async def street(message: types.Message):
    await message.answer('Можно сходить в кино/театр, можно весело провести время катаясь на коньках.'
                         'В холодную погоду не помешает выпить кофе/чая. Также можно пройтись по прекрасному парку,'
                         'а в конце вечера можно сходить покушать пиццы', reply_markup=help_assistant_street)


@dp.message_handler(Text(equals='Узнать погоду в городе🌤', ignore_case=True))
async def back(message: types.Message):
    await message.answer('Погода на сегодня ожидается...', reply_markup=user_kb)


@dp.message_handler(Text(equals='Сыграть в игру🔮', ignore_case=True))
async def game(message: types.Message):
    global count_of_attempts, number

    if count_of_attempts == 1:
        await message.answer(f'Отгадай число \nя загадал число от 1 до 20, попробуй его угадать😉', reply_markup=menu)
    else:
        await message.answer(f'Введите число🧐')


@dp.message_handler(Text(equals='Выйти в главное меню📋', ignore_case=True))
async def back(message: types.Message):
    await message.answer('секунду⏱', reply_markup=house_or_street)


@dp.message_handler(Text(equals='Как можно провести время на улице ?🚶‍♂🚶‍♀', ignore_case=True))
async def back_street(message: types.Message):
    await message.answer('Сейчас подскажу', reply_markup=help_assistant_street)


@dp.message_handler(Text(equals='Что можно поделать дома ?🏠', ignore_case=True))
async def back_street(message: types.Message):
    await message.answer('Сейчас подскажу', reply_markup=help_assistant_house)


# @dp.message_handler(Text(equals='Что за акция на пиццу?🍕', ignore_case=True))
# async def pizza(message: types.Message):
#     await message.answer(f'{list_pizza}')


@dp.message_handler(Text(equals='Какой фильм можно посмотреть?🎬', ignore_case=True))
async def kinogo(message: types.Message):
    for i in all_kinogo[1:4]:
        await message.answer(f'Название: {i[0]} \nCсылка: {i[-1]}')
    # g = 1
    # while True:
    #     if g < 10:
    #         for i in kinogo_decription, r in kinogo_urls:
    #             await message.answer(f'Название: {i} \nCcылка: {r}\n')
    #             g += 1
    #             print(g)
    #             break
    #     else:
    #         g += 1
    #         print(g)
    #         break

            # if i[1] == i[8] and r[1] == r[8]:
            #     break
            # else:
            #     await message.answer(f'Название: {i} \nCcылка: {r}\n')


@dp.message_handler(Text(equals='Какую книгу можно почитать?📚', ignore_case=True))
async def book(message: types.Message):
    for i in all_books[1:4]:
        await message.answer(f'Название:{i[0]} \nCcылка: {i[-1]}\n')


@dp.message_handler(Text(equals='Какой десерт можно легко приготовить?🧁', ignore_case=True))
async def cook(message: types.Message):
    for i in all_cooks[1:4]:
        await message.answer(f'Название: {i[0]} \nCcылка: {i[-1]}\n')


@dp.message_handler(Text(equals='На какой фильм в кинотеатр можно сходить ?🎬', ignore_case=True))
async def cinema(message: types.Message):
    for i in all_cinema[1:4]:
        await message.answer(f'Название: {i[0]} \nCcылка: {i[1]} \nСтоимость: {i[2]} \nДата: {i[-1]}', reply_markup=types.ReplyKeyboardRemove())
    await message.answer(f'Добавлена новая функция❗ \nМожно узнать о ближайшей кинотеатре который находится возле тебя'
                         f' \nФункция работает только на телефоне',
                         reply_markup=me_location)


@dp.message_handler(content_types=["location"])
async def location_cinema(message: types.Message):
    if message.location is not None:
        geolocation_me_cinema = (message.location.latitude, message.location.longitude)
        me_cinema.append(geolocation_me_cinema)
        ab_cinema = loc_geo_cinema[:]
        print(ab_cinema)
        ab_cinema.append(geolocation_me_cinema)
        ab_cinema.sort()
        print(ab_cinema)
        ab_index_cinema = ab_cinema.index(geolocation_me_cinema) - 1 if ab_cinema.index(geolocation_me_cinema) > 0 else 1
        print(ab_index_cinema)
        spend_cinema = (ab_cinema[ab_index_cinema])
        print(spend_cinema)
        await bot.send_location(message.chat.id, spend_cinema[0], spend_cinema[1], reply_markup=help_assistant_street)

        nom = Nominatim(user_agent='user')
        location_address = nom.reverse(spend_cinema)
        await message.answer(f'Находится: {location_address}')


@dp.message_handler(Text(equals='Куда можно сходить поесть ?🍽', ignore_case=True))
async def restaurant(message: types.Message):
    for i in all_pizza[1:4]:
        await message.answer(f'Название: {i[0]} \nCcылка: {i[1]} \nНаходится: {i[2]} '
                             f'\nВремя работы: {i[-1]}')


@dp.message_handler(Text(equals='Где и какой кофе можно выпить?☕️', ignore_case=True))
async def coffee(message: types.Message):
    for i in all_coffee[1:4]:
        await message.answer(f'Название: {i[0]} \nCcылка: {i[1]} \nАдрес: {i[-1]}', reply_markup=types.ReplyKeyboardRemove())
    await message.answer(f'Добавлена новая функция❗ \nМожно узнать о ближайшей кофейни которая находится возле тебя'
                         f' \nФункция работает только на телефоне',
                         reply_markup=me_location)


@dp.message_handler(content_types=["location"])
async def location(message):
    if message.location is not None:
        geolocation_me = (message.location.latitude, message.location.longitude)
        print(geolocation_me)
        me.append(geolocation_me)
        ab = loc_geo[:]
        print(ab)
        ab.append(geolocation_me)
        ab.sort()
        print(ab)
        ab_index = ab.index(geolocation_me) + 1 if ab.index(geolocation_me) > 0 else 0
        print(ab_index)
        spend = (ab[ab_index])
        print(spend)
        await bot.send_location(message.chat.id, spend[0], spend[1], reply_markup=help_assistant_street)

        nom = Nominatim(user_agent='user')
        location_address = nom.reverse(spend)
        await message.answer(f'Находится: {location_address}')

# @dp.message_handler(Text(equals='Узнать ближайшее местоположение кофейни', ignore_case=True))
# async def location(message: types.Message):
#     if message.location is not None:
#         geolocation_me = (message.location.latitude, message.location.longitude)
#
#         for i in l:
#             distance = h3.point_dist(geolocation_me, i, unit='m')  # to get distance in meters
#             metrix = (round(distance))
#             print(f'Дистанция между точка {metrix} m')
#             metrix_1.append(metrix)
#         await message.answer(min(metrix_1))


    # Подключить машинное состояние и записать в бд, после будем сравнивать как местоположение кофейни и пользователя

    # await message.answer(f'Название: {coffee_title[0]} \nCcылка: {coffee_urls[0]}')
    # await message.answer(f'Название: {coffee_title[1]} \nCcылка: {coffee_urls[1]}')
    # await message.answer(f'Название: {coffee_title[2]} \nCcылка: {coffee_urls[2]}')
    # await message.answer(f'Название: {coffee_title[3]} \nCcылка: {coffee_urls[3]}')

# @dp.message_handler(Text(equals='Какое представление можно посмотреть?', ignore_case=True))
# async def theatre(message: types.Message):
#     await message.answer(f'Название: {theatre_title[0]} \n{theatre_urls[0]} \nАдрес: {theatre_address[0]}'
#                          f'\nНачало:{theatre_time[0]} \nCтоимость: {theatre_cash[0]}')
#     await message.answer(f'Название: {theatre_title[1]} \n{theatre_urls[1]} \nАдрес: {theatre_address[1]}'
#                          f'\nНачало: {theatre_time[1]} \nCтоимость: {theatre_cash[1]}')
#     await message.answer(f'Название: {theatre_title[2]} \n{theatre_urls[2]} \nАдрес: {theatre_address[2]}'
#                          f'\nНачало: {theatre_time[2]} \nCтоимость: {theatre_cash[2]}')
#     await message.answer(f'Название: {theatre_title[3]} \n{theatre_urls[3]} \nАдрес: {theatre_address[3]}'
#                          f'\nНачало: {theatre_time[3]} \nCтоимость: {theatre_cash[3]}')

@dp.message_handler()
async def info(message: types.Message):
    global number, count_of_attempts

    try:
        if int(message.text) == number:
            await message.answer(f'Вы угадали!🎉\nКоличество попыток: {count_of_attempts}')
            number = random.randint(1, 20)

        elif int(message.text) < number:
            await message.answer(f'Введенное число меньше загаданного')
            count_of_attempts += 1
            await game(message)

        else:
            await message.answer(f'Введенное число больше загаданного')
            count_of_attempts += 1
            await game(message)
    except ValueError:
        await message.answer(f'Ошибка❗\nДанные должны иметь числовой тип')
        await game(message)

        # if g < 10:
        #         youi = [int(g) for i in kinogo_decription if g < 10]
        #         youi_1 = [int(g) for r in kinogo_decription if g < 10]
        #         await message.answer(f'Название: {r} \nCcылка: {i}\n')
        #         break
        #     else:
        #         g += 1
        #         print(g)
