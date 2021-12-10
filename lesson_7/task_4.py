# coding=utf-8
#
# Задание 4.
# Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }

# Понимание то что расмотрели на занятиях.
import os
#
# files = []
# for r, d, f in os.walk('./'):
#     for file in f:
#         file_path = os.path.join(r, file)
#         files.append(os.stat(file_path).st_size)
# max_size = max(files)
#
# i = 1
# out_dict = {}
#
# for _ in range(len(str(max_size))):
#     i *= 10
#     out_dict[i] = 0
#
# for file in files:
#     out_dict[10 ** len(str(file))] += 1
#
#
# print(out_dict)

#  Моёрешение задачи не уверен что правельно.


def show_stat(folder_path):
    stat = get_stat(folder_path)
    a = dict(sorted(stat.items(), reverse=False, key=lambda x: x[0]))
    print(a)


def get_stat(folder_path):
    stat = {}
    for root, _, files in os.walk(folder_path):
        for file in files:
            size = os.stat(os.path.join(root, file)).st_size
            key = 10 ** len(str(size))
            if key in stat:
                stat[key] += 1
            else:
                stat[key] = 1
    if stat == {}:
        raise Exception('В директории нет файлов')
    return stat


if __name__ == '__main__':
    try:
        my_folder_path = './'
        show_stat(my_folder_path)
    except Exception as e:
        print(e)
