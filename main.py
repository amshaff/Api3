import requests


print ("Напишите номер оного из представленных альбомов:\n"
    "17-Кукрыниксы; 18-Расскрашенная душа; \n"
       "19-Cтолкновение; 20-Фаворит солнца; \n"
       "21-Шаман; 22 - ХХХ; 23-Всадники света; \n "
       "24-MYSELF; 25-Горшенев-Есенин Душа Поэта; \n"
       "26-Горшенев-Есенин Смерть поэта; 232-Сингл Экклезиаст;\n"
       " 354-Вера, Надежда, Любовь; 622-Артист;")
def get_data_from_website():
    num = int(input())
    url = f'https://www.kukry.ru/disc/pub{num}'
    response = requests.get(url)

    if response.status_code == 200:
        # Извлечение заголовка страницы
        start_index = response.text.find('<title>') + len('<title>')
        end_index = response.text.find('</title>', start_index)
        title = response.text[start_index:end_index]

        return [title, url]
    else:
        return 'Error: Unable to fetch data from the website'


# Пример запуска функции и вывод результата
data = get_data_from_website()
print(*data, sep='\n')