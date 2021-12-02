# coding=utf-8
#
# Задание 2.
# *(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# для получения информации вида: (<remote_addr>, <request_datetime>, <request_type>,
# <requested_resource>, <response_code>, <response_size>):


import re
import requests
# Записываем регулярное выражения:
PAD = re.compile(r'((?:[0-9]{,3}[.]){3}[0-9]{,3}) - - '
                 r'(.[0-9]{,2}/\w+/[0-9]{4}:(?:[0-9]{2}:){2}[0-9]{2} \+[0-9]{4}]) .(\w+) '
                 r'([/\w+]{0,}) (?:[^\"]*)\" ([0-9]+) ([0-9]+)')
# Записали адрес в переменную.
url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
# Делаем get запрос по адресу и переобразуем в текст.
content = requests.get(url).text
# Проходим циклом по полученным логам. При помощи функции findall()
# Строка сканируется слева направо, и совпадения возвращаются в найденном порядке.
for arg in PAD.findall(content):
    addr, datetime, r_type, resource, code, size = arg
    print(addr, datetime, r_type, resource, code, size)
