from bs4 import BeautifulSoup
import requests

headers = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0'
}

theatre_urls = []
theatre_title = []
theatre_address = []
theatre_time = []
theatre_cash = []


def theatre():
    url = f'https://afisha.relax.by/theatre/gomel/'

    response = requests.get(url=url, headers=headers)

    pages_info = BeautifulSoup(response.text, 'html.parser')

    performance = pages_info.find_all('div', class_='schedule__list')
    for city_theatre in performance:
        urls = city_theatre.find('div', class_='schedule__event-block').find('a').get('href')
        title = city_theatre.find('div', class_='schedule__event-block').find('a').text
        address = city_theatre.find('div', class_='schedule__place schedule__place--fill').find('span').text
        time = city_theatre.find('div', class_='schedule__seance-wrap').find('a').text
        cash = city_theatre.find('div', class_='schedule__seance-wrap').find('span').text

        theatre_urls.append(urls)
        theatre_title.append(title)
        theatre_address.append(address)
        theatre_time.append(time)
        theatre_cash.append(cash)

    return theatre_urls, theatre_title, theatre_address, theatre_time, theatre_cash


theatre()
