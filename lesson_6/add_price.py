# coding=utf-8
# Задание 6.
#
# Реализовать простую систему хранения данных о суммах продаж булочной.
# Должно быть два скрипта с интерфейсом командной строки:
# Скрип для добавление данных в фаил buns.csv

import sys
price = ''.join(sys.argv[1:])
with open('bakery.csv', 'a', encoding='utf-8') as file:
    file.write(price + '\n')
