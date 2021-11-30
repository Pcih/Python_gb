# Зададние 3
#
# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом
# — данные об их хобби. Известно, что при хранении данных используется принцип:
# одна строка — один пользователь, разделитель между значениями — запятая.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
# ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл.
# Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей,
# чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.

from itertools import zip_longest
import json

my_dict = {}

with open('users.csv'.encode('utf-8')) as user:
    with open('hobby.csv'.encode('utf-8')) as hobby:
        num_user_line = sum(1 for line in user)
        num_hobby_line = sum(1 for line in hobby)

        if num_user_line < num_hobby_line:
            exit(1)
        user.seek(0)
        hobby.seek(0)
        for line_user, line_user_hobby in zip_longest(user, hobby):
            my_dict[line_user.strip()] = line_user_hobby.strip() if line_user_hobby is not None else line_user_hobby

with open('task_3.json', 'w', encoding='utf-8') as file:
    json.dump(my_dict, file, ensure_ascii=False)
print(my_dict)
