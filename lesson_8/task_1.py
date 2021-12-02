# coding=utf-8
#
# Задание 1.
# Написать функцию email_parse(<email_address>),
# которая при помощи регулярного выражения извлекает
# имя пользователя и почтовый домен из email адреса
# и возвращает их в виде словаря. Если адрес не валиден,
# выбросить исключение ValueError.


import re

# Такая же регулярка как у вас толко в вашей не учитывались адресса pcih-1984@mail.com
# он брал толко то что с право от дефиса а с лево выкидывал и добавил обработку заглавнх букв.

EMAIL = re.compile(r'([A-Za-z-0-9_\.]+)@([a-z0-9]+\.[a-z]+)')

# address = input('Введите e-mail: ') - реализовал ввод адреса в ручную.

def email_parse(email):
    found_info = EMAIL.findall(email)
    if len(found_info) != 0:
        name, addr = found_info[0]
    else:
        raise ValueError(f'wrong email: {email}')
    print(name, addr)

email_parse('maximka@mail.ru')
email_parse('front@mailmailcom')

#  Просто дополнение к программе чтоб она не писала много строк.
#
# try:
#     email_parse(address)
#
# except BaseException as err:
#     print(err)

