# 5. Создать список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]

# 1. Вывести на экран эти цены через запятую в одну строку, 
# цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»). 
# Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, 
# получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# 
# 2. Вывести цены, отсортированные по возрастанию, новый список не создавать 
# (доказать, что объект списка после сортировки остался тот же).
# 
# 3. Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# 
# 4. Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

# 1. Создал список для работы и вывел id для сравнения из 2-го пункта.
price_list = [99.7, 4.33, 15.1, 23.5, 77.3, 112.23, 12.22, 55.2, 12.1, 147.12]
price_new = ""
print(id(price_list))

# Циклом прохожу по каждому элементу и отделяю рубли от копеек.
for i in price_list:
    rub_pice = i // 1
    kop_prici = i % 1 * 100
    rub_prici_new = str(round(rub_pice))
    kop_prici_new = str(round(kop_prici))
    # Формирую строку для вывода информации.
    price_new = price_new + (f' "Цена {rub_prici_new} руб. {kop_prici_new} коп.", ') 
    #  print(f'"Цена {round(rub_pice)} руб. {round(kop_prici)} коп."') # Если выводить в список, а не в строчку.
print(price_new)
print('Список без именений.')
print(" ")

# 2. Отсортировал список по возрастанию.
# Для таких целей луче была бы функция но мы пока её не изучали.
price_list.sort()
price_new = ""
print(id(price_list))
for i in price_list:
    rub_pice = i // 1
    kop_prici = i % 1 * 100
    rub_prici_new = str(round(rub_pice))
    kop_prici_new = str(round(kop_prici))
    price_new = price_new + (f' "Цена {rub_prici_new} руб. {kop_prici_new} коп." ')
print(price_new)
print('Список по возростанию.')
print(" ")


# 3. Отсортировал список по убыванию.
price_list.sort(reverse=True)
price_new = ""
print(id(price_list))
for i in price_list:
    rub_pice = i // 1
    kop_prici = i % 1 * 100
    rub_prici_new = str(round(rub_pice))
    kop_prici_new = str(round(kop_prici))
    price_new = price_new + (f' "Цена {rub_prici_new} руб. {kop_prici_new} коп." ')
print(price_new)
print('Список по убыванию.')
print(" ")

# 4. Вывел 3 самые дорогие позиции.
price_list.sort(reverse=True)
i = 0
price_new = ""
print(id(price_list))
while i < 5:    
    rub_pice = price_list[i] // 1
    kop_prici = price_list[i] % 1 * 100
    rub_prici_new = str(round(rub_pice))
    kop_prici_new = str(round(kop_prici))
    price_new = price_new + (f' "Цена {rub_prici_new} руб. {kop_prici_new} коп." ')
    i += 1 
print(price_new)
print(f'Список {i} самые дорогие позиции ')
print(" ")