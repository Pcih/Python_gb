# Задание 2

import requests
from decimal import Decimal


def currency_rates(currency_code):
    response = requests.get(r'http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding=response.encoding)
    for el in content.split('<CharCode>')[1:]:
        char_code = el[:3]
        value = (el.split('<Value>')[1:][0].split('</Value>')[0])
        value = Decimal(f'{value.split(",")[0]}.{value.split(",")[1]}')
        nominal = Decimal(el.split('<Nominal>')[1:][0].split('</Nominal>')[0])
        course = value / nominal
        if currency_code.upper() == char_code:
            return course


print(currency_rates('usd'))
print(currency_rates('AZN'))
print(currency_rates('12'))