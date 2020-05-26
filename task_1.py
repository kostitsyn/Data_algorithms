# Решение задачи №4 из урока №3

import random
import timeit
import cProfile


def get_array(n):
    """Возвращает массив от 0 до 5 с заданным параметром - размером массива n"""
    MIN_ITEM = 0
    MAX_ITEM = 5
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(n)]
    return array


def commonest_num_1(n):
    """Первая (исходная) функция, без использования встроенных функций"""
    arr = get_array(n)
    max_replace = 0
    for i in arr:
        counter = 0
        for j in arr:
            if i == j:
                counter += 1
        if counter > max_replace:
            max_replace = counter
            num = i
    if max_replace == 1:
        return 'Все значения уникальны'
    else:
        return num


def commonest_num_2(n):
    """Вторая функция, решение с использованием множества и функции count"""
    arr = get_array(n)
    my_set = set(arr)
    max_replace = 0
    for i in my_set:
        counter = arr.count(i)
        if counter > max_replace:
            max_replace = counter
            num = i
    if max_replace == 1:
        return 'Все значения уникальны'
    else:
        return num


def commonest_num_3(n):
    """Третья функция, решение с использованием сортировки"""
    arr = get_array(n)
    arr.sort()
    num = arr[0]
    counter = 0
    max_replace = 0
    for i in arr:
        if i != num:
            counter = 0
            num = i
        counter += 1
        if counter > max_replace:
            max_replace = counter
            number = i
    if max_replace == 1:
        return 'Все значения уникальны'
    else:
        return number


print(timeit.timeit('commonest_num_1(1)', number=100, globals=globals()))  # 0.0006870259999999934
print(timeit.timeit('commonest_num_1(10)', number=100, globals=globals()))  # 0.004626686000000005
print(timeit.timeit('commonest_num_1(100)', number=100, globals=globals()))  # 0.07595236800000002
print(timeit.timeit('commonest_num_1(1000)', number=100, globals=globals()))  # 4.043639022000001

print(timeit.timeit('commonest_num_2(1)', number=100, globals=globals()))  # 0.0002258009999999977
print(timeit.timeit('commonest_num_2(10)', number=100, globals=globals()))  # 0.0012916229999999917
print(timeit.timeit('commonest_num_2(100)', number=100, globals=globals()))  # 0.010530880000000006
print(timeit.timeit('commonest_num_2(1000)', number=100, globals=globals()))  # 0.104304244
print(timeit.timeit('commonest_num_2(10000)', number=100, globals=globals())) # 1.051329422
print(timeit.timeit('commonest_num_2(100000)', number=100, globals=globals())) # 10.541218231

print(timeit.timeit('commonest_num_3(1)', number=100, globals=globals()))  # 0.00021714100000000403
print(timeit.timeit('commonest_num_3(10)', number=100, globals=globals()))  # 0.001234531000000004
print(timeit.timeit('commonest_num_3(100)', number=100, globals=globals()))  # 0.011158249000000002
print(timeit.timeit('commonest_num_3(1000)', number=100, globals=globals()))  # 0.10844981900000002
print(timeit.timeit('commonest_num_3(10000)', number=100, globals=globals())) # 1.1277228080000001
print(timeit.timeit('commonest_num_3(100000)', number=100, globals=globals())) # 11.047815708

cProfile.run('commonest_num_1(1000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#    1    0.000    0.000    0.042    0.042 <string>:1(<module>)
# 1000    0.001    0.000    0.001    0.000 random.py:200(randrange)
# 1000    0.000    0.000    0.002    0.000 random.py:244(randint)
# 1000    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
#    1    0.000    0.000    0.002    0.002 task_1.py:12(<listcomp>)
#    1    0.040    0.040    0.042    0.042 task_1.py:16(commonest_num_1)
#    1    0.000    0.000    0.002    0.002 task_1.py:8(get_array)

cProfile.run('commonest_num_2(100000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.207    0.207 <string>:1(<module>)
# 100000    0.063    0.000    0.131    0.000 random.py:200(randrange)
# 100000    0.035    0.000    0.165    0.000 random.py:244(randint)
# 100000    0.049    0.000    0.068    0.000 random.py:250(_randbelow_with_getrandbits)
#      1    0.031    0.031    0.197    0.197 task_1.py:12(<listcomp>)
#      1    0.001    0.001    0.207    0.207 task_1.py:34(commonest_num_2)
#      1    0.000    0.000    0.197    0.197 task_1.py:8(get_array)

cProfile.run('commonest_num_3(100000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.220    0.220 <string>:1(<module>)
# 100000    0.066    0.000    0.135    0.000 random.py:200(randrange)
# 100000    0.036    0.000    0.172    0.000 random.py:244(randint)
# 100000    0.050    0.000    0.069    0.000 random.py:250(_randbelow_with_getrandbits)
#      1    0.032    0.032    0.204    0.204 task_1.py:12(<listcomp>)
#      1    0.009    0.009    0.220    0.220 task_1.py:50(commonest_num_3)
#      1    0.000    0.000    0.204    0.204 task_1.py:8(get_array)

''' Вывод: вариант 1 получился с асимптотикой O(n**2), поскольку в нём присутствуют два вложенных цикла; время выполнения
до n = 100 росло линейно, далее наблюдается большой прирост времени. Проблемное место - алгоритм двойного перебора
массива.
Вариант 2 и вариант 3 имеют асимпототику O(n), вариант 2 с алогиритмом использования множества и функции count
получился незначительно быстрее варианта 3 с использованием функции сортировки. Проблемные места во втором и третьем 
варианте - генерация списка'''
