# coding=utf-8
#
# Задание 5.
# *(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде
# словаря, в котором ключи те же, а значения — кортежи вида
# (<files_quantity>, [<files_extensions_list>]), например:
#     {
#       100: (15, ['txt']),
#       1000: (3, ['py', 'txt']),
#       10000: (7, ['html', 'css']),
#       100000: (2, ['png', 'jpg'])
#     }

import os
import json

files = []
for r, d, f in os.walk('./'):
    for file in f:
        file_path = os.path.join(r, file)
        files.append((file_path.split('.')[-1], os.stat(file_path).st_size))
max_size = max(files, key=lambda x: x[1])[1]

i = 1
out_dict = {}

for _ in range(len(str(max_size))):
    i *= 10
    out_dict[i] = (0, [])

for file in files:
    num, ext_list = out_dict[10 ** len(str(file[1]))]
    ext_list.append(file[0])
    ext_list = list(set(ext_list))
    out_dict[10 ** len(str(file[1]))] = (num + 1, ext_list)

print(out_dict)

with open(os.path.basename(os.getcwd()) + '_summary.json', 'w') as f_json:
    json.dump(out_dict, f_json)


# Сломал окончательно :( буду думать.

# def show_stat(folder_path):
#     stat = get_stat(folder_path)
#     a = dict(sorted(stat.items(), reverse=False, key=lambda x: x[0]))
#     print(a)
#     with open(os.path.basename(os.getcwd()) + '_summary.json', 'w') as f_json:
#         json.dump(a, f_json)
#
#
#
# def get_stat(folder_path):
#     stat = {}
#     ext_list = 0
#     for root, _, files in os.walk(folder_path):
#         for file in files:
#             print(file)
#             file.split('.')
#             ext_list.append(file[0])
#             ext_list = list(set(ext_list))
#             size = os.stat(os.path.join(root, file)).st_size
#             key = 10 ** len(str(size))
#             if key in stat:
#                 stat[key] += 1
#             else:
#                 stat[key] = 1
#     if stat == {}:
#         raise Exception('В директории нет файлов')
#     return stat
#
#
# if __name__ == '__main__':
#     try:
#         my_folder_path = './'
#         show_stat(my_folder_path)
#     except Exception as e:
#         print()