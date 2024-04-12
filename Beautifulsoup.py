import requests
from bs4 import BeautifulSoup

# Получение данных с веб-страницы и парсинг XML
url_cbr = "http://www.cbr.ru/scripts/XML_daily.asp"
response_cbr = requests.get(url_cbr)
soup_cbr = BeautifulSoup(response_cbr.content, 'xml')

# Извлечение информации из XML
currency_names = soup_cbr.find_all('Name')
for name in currency_names:
    print(name.text)

# Получение данных с веб-страницы и парсинг HTML
url_matplotlib = "https://matplotlib.org/stable/gallery/index.html"
response_matplotlib = requests.get(url_matplotlib)
soup_matplotlib = BeautifulSoup(response_matplotlib.content, 'html.parser')

# Извлечение информации из HTML
h2_elements = soup_matplotlib.find_all('h2')
for h2 in h2_elements:
    print(h2.text.strip())

# Очистка найденных элементов от HTML-тегов
std_ref_elements = soup_matplotlib.find_all(class_='std std-ref')
for std_ref in std_ref_elements:
    print(std_ref.text.strip())
    
