from bs4 import BeautifulSoup
import requests
from New_life_3.buttons import cities, user_kb

film_urls = []
title_film = []
time_film = []
cash_film = []

city = input('Введите ваш город')


def cinema():
    url = f'https://bycard.by/afisha/{city}/kino?view=top'

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
print(all_cinema)
