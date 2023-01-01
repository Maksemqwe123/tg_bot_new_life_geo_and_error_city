from bs4 import BeautifulSoup
import requests
import re

headers = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0'
}
coffee_urls = []
coffee_title = []
coffee_address = []
recond = []


def coffee_city():
    url = 'https://www.relax.by/cat/ent/coffee/gomel/'

    response = requests.get(url=url, headers=headers)

    pages_info = BeautifulSoup(response.text, 'html.parser')

    coffee_shops = pages_info.find_all('div', class_='Place__headerContent')
    for coffee in coffee_shops:
        urls = coffee.find('div', class_='Place__titleWrapper').find('div', class_='Place__mainTitle').find('a').get('href')
        title = coffee.find('div', class_='Place__titleWrapper').find('div', class_='Place__mainTitle').find('a').text
        address = coffee.find('div', class_='Panel Place__content Place__content--address').find('div', class_='Place__content-inner').find('div', class_='Place__meta').find('span', class_='Place__addressText').text

        coffee_urls.append(urls)
        coffee_title.append(title)
        line = re.sub('Гомель, ул. Жемчужная, 26[а]', 'Гомель, ул. Жемчужная, 26', address)
        lines = re.sub('Гомель, пр-т Космонавтов, 61', 'Гомель, Космонавтов, 61', line)
        lines_1 = re.sub('Гомель, ул. Ильича, 51Г', 'Гомель, ул. Ильича, 51', lines)
        coffee_address.append(lines_1)
        recond.append(coffee_address[:-1])

    return coffee_urls, coffee_title, coffee_address


coffee_city()
all_coffee = list(zip(coffee_title, coffee_urls, coffee_address))
