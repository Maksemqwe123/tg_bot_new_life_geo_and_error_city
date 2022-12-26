from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import h3
from geolocation import loc_geo
metrix_1 = []


bot = Bot('5587641606:AAGVMc75T2zaq_GovxKy0nn8wiKFAKBbOvg')
dp = Dispatcher(bot)

me = []

@dp.message_handler(commands='start')
async def geo(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_geo)
    keyboard_1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo_1 = types.KeyboardButton(text="Узнать ближайшую кофе", request_location=loc_geo)
    keyboard_1.add(button_geo_1)
    await bot.send_message(message.chat.id, "Привет! Нажми на кнопку и передай мне свое местоположение", reply_markup=keyboard)


@dp.message_handler(content_types=["location"])
async def location(message):
    if message.location is not None:
        geolocation_me = (message.location.latitude, message.location.longitude)
        me.append(geolocation_me)
        print(geolocation_me)
        ab = loc_geo[:]
        ab.append(geolocation_me)
        ab.sort()
        ab_index = ab.index(geolocation_me) - 1 if ab.index(geolocation_me) > 0 else 0
        spend = (ab[ab_index])
        print(spend[0])
        await bot.send_location(message.chat.id, spend[0], spend[1])

        # for i in l:
        #     ab = l[:]
        #     ab.append(geolocation_me)
        #     ab.sort()
        #     ab_index = ab.index(geolocation_me) - 1 if ab.index(geolocation_me) > 0 else 0
        #     spend = (ab[ab_index])
        #     print(spend)


        #     distance = h3.point_dist(geolocation_me, i, unit='m')  # to get distance in meters
        #     # print(i, round(distance))
        #     metrix = (round(distance))
        #     print(f'Дистанция между точка {metrix} m')
        #     metrix_1.append(metrix)
        # print(min(metrix_1))


# def location(message):
#     if message.location is not None:
#         print(message.location)
#         print("latitude: %s; longitude: %s" % (message.location.latitude, message.location.longitude)

if __name__ == '__main__':
    print('bot polling started')
    executor.start_polling(dp, skip_updates=True)
# latitude: 52.473507; longitude: 31.02713



# import telebot
# from telebot import types
# bot = telebot.TeleBot('5587641606:AAGVMc75T2zaq_GovxKy0nn8wiKFAKBbOvg')
#
#
# @bot.message_handler(commands=["start"])
# def start (message):
#     #Клавиатура с кнопкой запроса локации
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
#     keyboard.add(button_geo)
#     bot.send_message(message.chat.id, "Поделись местоположением", reply_markup=keyboard)
#
#  #Получаю локацию
# @bot.message_handler(content_types=['location'])
# def location (message):
#     if message.location is not None:
#         print(message.location)
#         print(message)
#
# bot.polling(none_stop = True)
# input()

# Отдать с начала пользователю долготу и шыроту, а потом запросить координаты, чтобы показать его геолокацию