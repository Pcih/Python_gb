# coding=utf-8

# Задание 1.
# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
#
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp

# Решил разобраться тот пример который был в разборе домашнего задания.
# Создал словарь не посредственно в кода.
import os
#
# # Создали словарь для хранения структуры создаваемых папок.
# cliche = {'my_progect': ['setting', 'mainapp', 'adminapp', 'authapp']}
#
# # Циклом прохожу по славарю.
# for root, folders in cliche.items():
#     if os.path.exists(root):
#         print(root, 'folder exists now')
#     else:
#         for folder in folders:
#             new_dir = os.path.join(root, folder)
#             os.makedirs(new_dir)

# Тот же вариант только уже шаблон храню в файле json

# import json
#
# with open("task_1.json") as write_file:
#     cliche = json.load(write_file)
#     for root, folders in cliche.items():
#         if os.path.exists(root):
#             print(root, 'folder exists now')
#         else:
#             for folder in folders:
#                 new_dir = os.path.join(root, folder)
#                 os.makedirs(new_dir)

# Попробовал обеденить функции, работу с системой и исключения.
from shutil import rmtree


def create_starter(dir_path, dir_name, folders):
    current_path = os.path.join(dir_path, dir_name)
    if not os.path.exists(current_path):
        os.mkdir(current_path)
    for folder in folders:
        current_folder = os.path.join(current_path, folder)
        if not os.path.exists(current_folder):
            os.mkdir(current_folder)


def destroy_starter(dir_path, dir_name):
    current_path = os.path.join(dir_path, dir_name)
    rmtree(current_path)


if __name__ == '__main__':
    my_name = 'my_first_project'
    my_path = './'
    my_folders = ('settings', 'mainapp', 'adminapp', 'authapp')
# Обработал исключения.
    try:
        create_starter(my_path, my_name, my_folders)
        # destroy_starter(my_path, my_name)
    except Exception as e:
        print(e)
