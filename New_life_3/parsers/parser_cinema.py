# from bs4 import BeautifulSoup
# import requests
# from New_life_3.bot_location import *
#
# film_urls = []
# title_film = []
# time_film = []
# cash_film = []
#
#
# @dp.message_handler(state=Test.Q2)
# async def answer_q1(message: types.Message, state: FSMContext):
#     data = await state.get_data()
#     answer1 = data.get("answer1")
#     answer2 = message.text
#
#
# url = f'https://bycard.by/afisha/{poi}/kino?view=top'
#
# response = requests.get(url=url)
#
# pages_info = BeautifulSoup(response.text, 'html.parser')
#
# films = pages_info.find_all('a', class_='capsule')
#
# for film in films:
#     urls = film.get('href')
#     title = film.find('p', class_='capsule__title').text
#     time = film.find('p', class_='capsule__date').text
#     cash = film.find('p', class_='capsule__price').text
#
#     film_urls.append('https://bycard.by' + urls.strip())
#     title_film.append(title.strip())
#     time_film.append(time.strip())
#     cash_film.append(cash.strip())
#
#     await message.answer("Привет")
#
#     await state.reset_state(with_data=False)
#
#
# all_cinema = list(zip(title_film, film_urls, cash_film, time_film))
#
#
# @dp.message_handler(commands='kinogo')
# async def kinogo111(message: types.Message):
#     for i in all_cinema:
#         await message.answer(f'Название: {i[0]} \nCcылка: {i[1]} \nСтоимость: {i[2]} \nДата: {i[-1]}')


from bs4 import BeautifulSoup
import requests

film_urls = []
title_film = []
time_film = []
cash_film = []


def cinema():
    url = f'https://bycard.by/afisha/gomel/kino?view=top'

    response = requests.get(url=url)

    pages_info = BeautifulSoup(response.text, 'html.parser')

    films = pages_info.find_all('a', class_='capsule')

    for film in films:
        urls = film.get('href')
        title = film.find('p', class_='capsule__title').text
        time = film.find('p', class_='capsule__date').text
        cash = film.find('p', class_='capsule__price').text

        film_urls.append('https://bycard.by' + urls.strip())
        title_film.append(title.strip())
        time_film.append(time.strip())
        cash_film.append(cash.strip())

    return title_film, film_urls, cash_film, time_film


parser_cinema = cinema()
all_cinema = list(zip(title_film, film_urls, cash_film, time_film))
