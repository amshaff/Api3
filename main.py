import requests


def get_data_from_website():
    url = 'https://www.kukry.ru/disc/pub19'
    response = requests.get(url)

    if response.status_code == 200:
        # Извлечение заголовка страницы
        start_index = response.text.find('<title>') + len('<title>')
        end_index = response.text.find('</title>', start_index)
        title = response.text[start_index:end_index]

        return title
    else:
        return 'Error: Unable to fetch data from the website'


# Пример запуска функции и вывод результата
data = get_data_from_website()
print(data)
