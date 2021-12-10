# coding=utf-8
#
# Задание 3.
# Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:


import os
import shutil


# Пример расмотренный на уроке понял выариант решения.

files = []


def reform_dir(my_dir, folder):
    for r, d, f in os.walk(folder):
        for file in f:
            if '.html' in file:
                files.append(os.path.join(r, file))
    for path in files:
        folder_new = os.path.join(my_dir, os.path.basename(os.path.dirname(path)))
        if not os.path.exists(folder_new):
            os.mkdir(folder_new)
        save_path = os.path.join(folder_new, os.path.basename(path))
        shutil.copy(path, save_path)


if __name__ == '__main__':
    new_dir = 'task3'
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
    new_folder = r'my_second_project'
    try:
        reform_dir(new_dir, new_folder)
    except Exception as e:
        print(e)
        exit(1)

# Это моя попыта оптимизации кода но он у меня создаёт папку в нутри my_second_project

# def reform_dir(root_dir, search_file='index.html'):
#     # if os.path.exists(templates_path):
#     #     shutil.rmtree(templates_path)
#     for root, dirs, files in os.walk(root_dir):
#         # if root == templates_path:
#         #     break
#         if search_file in set(files):
#             templates_path = os.path.join('task3')
#             if not os.path.exists(templates_path):
#                 os.mkdir(templates_path)
#             found_dir = os.path.split(root)[1]
#             curr_path = os.path.join(templates_path, found_dir)
#             if not os.path.exists(curr_path):
#                 os.mkdir(curr_path)
#             for file in files:
#                 if not os.path.exists(os.path.join(curr_path, file)):
#                     shutil.copy2(os.path.join(root, file), curr_path)
#
#
# if __name__ == '__main__':
#     my_dir = './my_second_project'
#     my_file = 'base.html'
#     try:
#         reform_dir(my_dir)
#     except Exception as e:
#         print(e)
#         exit(1)
