# coding=utf-8
#
# Задание 3.
# Написать декоратор для логирования типов позиционных аргументов функции, например:

from functools import wraps
# Из билеотеки functools - это сборник функций высокого уровня. Мы берём декоратор wraps.
def type_logger(func):
    @wraps(func)
    # Оборачиваем декоратором что бы передать атрибуты основной функции.
    def wrapper(*args):
        for arg in args:
            print(f'{func.__name__}({arg}: {type(arg)})', end=', ')
        return func(*args)

    return wrapper

# Оборачиваем основную функцию декоратором 
@type_logger
def calc_cube(*args):
    """this shows only with 'from functools import wraps'"""
    return list(map(lambda x: x ** 3, args))


a = calc_cube(5, 3)
print(a)
print(calc_cube.__name__)
print(calc_cube.__doc__)