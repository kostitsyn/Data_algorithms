import math
import timeit
import cProfile


def sieve_erat(number):
    n = number * 100
    sieve = [i for i in range(n)]
    numerate_array = [i for i in range(1, n + 1)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i
    sieve_res = [i for i in sieve if i != 0]
    sieve_dict = dict(zip(numerate_array, sieve_res))
    return f'{number}-e простое число: {sieve_dict[number]}'


def my_sieve(number):
    array = [0]
    i = 2
    while True:
        if i == 2:
            array.append(i)
        for j in range(2, math.ceil(math.sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            array.append(i)
        if len(array) - 1 == number:
            break
        i += 1
    return f'{number}-e простое число: {array[number]}'


print(timeit.timeit('sieve_erat(1)', number=100, globals=globals()))  # 0.0027840999999999977
print(timeit.timeit('sieve_erat(10)', number=100, globals=globals()))  # 0.031884
print(timeit.timeit('sieve_erat(100)', number=100, globals=globals()))  # 0.37403830000000005
print(timeit.timeit('sieve_erat(1000)', number=100, globals=globals()))  # 4.3114083

print(timeit.timeit('my_sieve(1)', number=100, globals=globals()))  # 0.00014649999999999733
print(timeit.timeit('my_sieve(10)', number=100, globals=globals()))  # 0.0028070000000000005
print(timeit.timeit('my_sieve(100)', number=100, globals=globals()))  # 0.0534578
print(timeit.timeit('my_sieve(1000)', number=100, globals=globals()))  # 1.0529064

cProfile.run('sieve_erat(1000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1    0.004    0.004    0.004    0.004 task_2.py:10(<listcomp>)
# 1    0.003    0.003    0.003    0.003 task_2.py:18(<listcomp>)
# 1    0.031    0.031    0.042    0.042 task_2.py:7(sieve_erat)
# 1    0.003    0.003    0.003    0.003 task_2.py:9(<listcomp>)

cProfile.run('my_sieve(1000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#    1    0.000    0.000    0.015    0.015 <string>:1(<module>)
#    1    0.011    0.011    0.015    0.015 task_2.py:26(my_sieve)

"""Вывод: Оба варианта имеют асимптотику O(n**2), поскольку используют вложенные циклы, однако второй вариант
оказался быстрее. Проблемное место первого варианта - алгоритм самой функции"""