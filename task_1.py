# Использовал 5-е задание 3-го урока

import random
import sys
from _collections import deque

print('Находим максимальный отрицательный элемент в массиве')


def my_show(object):
    sum_ = 0
    id_list = deque()
    if hasattr(object, '__iter__'):
        if hasattr(object, 'items'):
            for key, value in object.items():
                if id(value) in id_list:
                    continue
                sum_ += sys.getsizeof(value)
                id_list.append(id(value))
                if hasattr(value, '__iter__'):
                    for k in value:
                        if id(k) in id_list:
                            continue
                        sum_ += sys.getsizeof(k)
                        id_list.append(id(k))
        elif not isinstance(object, str):
            for item in object:
                if id(item) in id_list:
                    continue
                sum_ += sys.getsizeof(item)
                id_list.append(id(item))
    return sum_


# Генерируем массив
SIZE = 8
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


# ----------------------------------------------------------------------------------------------------------------------
# Первый (исходный) вариант
def func_1(array):
    global lst
    temp_array = []
    for i in array:
        if i < 0:
            temp_array.append(i)
    max_neg_num = temp_array[0]
    for j in temp_array:
        if j > max_neg_num:
            max_neg_num = j
    print(f'Массив элементов: {array} Максимальный отрицательный элемент: '
          f'{max_neg_num}, его индекс: {array.index(max_neg_num)}')
    lst = locals()
    return lst


result = func_1(array)

print(f'Переменные первого (исходного) варианта занимают \033[1m{my_show(result)}\033[0m байт памяти. '
      f'Количество переменных {len(lst)}.\n')


# ----------------------------------------------------------------------------------------------------------------------
# Второй вариант, с использованием отрицательной бесконечности
def func_2(array):
    global lst
    max_neg_num = float('-inf')
    for i in array:
        if max_neg_num < i < 0:
            max_neg_num = i
    print(f'Массив элементов: {array} Максимальный отрицательный элемент: '
          f'{max_neg_num}, его индекс: {array.index(max_neg_num)}')
    lst = locals()
    return lst


result = func_2(array)
print(
    f'Переменные второго варианта с отрицательной бесконечностью занимают \033[1m{my_show(result)}\033[0m байт памяти. '
    f'Количество переменных {len(lst)}.\n')


# ----------------------------------------------------------------------------------------------------------------------
# Третий вариант, с использованием очереди и сортировки
def func_3(array):
    global lst
    ar_1 = sorted(deque(array))
    while True:
        max_neg_num = ar_1.pop()
        if max_neg_num < 0:
            break
    print(f'Массив элементов: {array} Максимальный отрицательный элемент: '
          f'{max_neg_num}, его индекс: {array.index(max_neg_num)}')
    lst = locals()
    return lst


result = func_3(array)

print(f'Переменные третьего варианта с очередью и сортировкой занимают \033[1m{my_show(result)}\033[0m байт памяти. '
      f'Количество переменных {len(lst)}.')
