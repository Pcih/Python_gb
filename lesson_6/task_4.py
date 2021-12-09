# Зададние 4
#
# *(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
# (разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
# Только теперь не нужно создавать словарь с данными.
# Вместо этого нужно сохранить объединенные данные в новый файл (users_hobby.txt).
# Хобби пишем через двоеточие и пробел после ФИО:
# Иванов,Иван,Иванович: скалолазание,охота
# Петров,Петр,Петрович: горные лыжи




from itertools import zip_longest


my_dict = {}
with open('task_4', 'w', encoding='utf-8') as file:
    with open('users.csv'.encode('utf-8')) as user:
        with open('hobby.csv'.encode('utf-8')) as hobby:
            num_user_line = sum(1 for line in user)
            num_hobby_line = sum(1 for line in hobby)

            if num_user_line < num_hobby_line:
                exit(1)
            user.seek(0)
            hobby.seek(0)
            for line_user, line_user_hobby in zip_longest(user, hobby):
                file.write(f'{line_user.strip()}: '
                           f'{line_user_hobby.strip() if line_user_hobby is not None else line_user_hobby } \n')


