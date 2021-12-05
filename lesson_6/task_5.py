# Зададние 5
#
# **(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки,
# чтобы можно было задать имя обоих исходных файлов и имя выходного файла.
# Проверить работу скрипта.


from itertools import zip_longest
import sys

user, hobby, stack = sys.argv[1:]
my_dict = {}
with open(stack, 'w', encoding='utf-8') as file:
    with open(user.encode('utf-8')) as user:
        with open(hobby.encode('utf-8')) as hobby:
            num_user_line = sum(1 for line in user)
            num_hobby_line = sum(1 for line in hobby)

            if num_user_line < num_hobby_line:
                exit(1)
            user.seek(0)
            hobby.seek(0)
            for line_user, line_user_hobby in zip_longest(user, hobby):
                file.write(f'{line_user.strip()}: '
                           f'{line_user_hobby.strip() if line_user_hobby is not None else line_user_hobby } \n')
