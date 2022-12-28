import argparse
import requests
from bs4 import BeautifulSoup

def get_weather(city):
    # Отправляем запрос на сайт и получаем HTML-страницу
    url = f"https://www.google.com/search?q=погода+{city}"
    r = requests.get(url)
    html = r.text

    # Используем Beautiful Soup для парсинга HTML-страницы
    soup = BeautifulSoup(html, "html.parser")

    # Получаем текущую температуру
    temperature_element = soup.find(class_="BNeawe iBp4i AP7Wnd")
    temperature = temperature_element.text

if __name__ == "__main__":
    # Создаем парсер аргументов командной строки
    parser = argparse.ArgumentParser()
    parser.add_argument("city", help="Город, для которого нужно узнать погоду")
    args = parser.parse_args()

    # Получаем и выводим погоду
    weather = get_weather(args.city)
    print(weather)
