import random

print('Находим сумму элементов, находящихся между минимальным и максимальным элементами')

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
max_num = array[0]
min_num = array[0]

print(f'Исходный список:\n{array}\n')

for index, value in enumerate(array):
    if value > max_num:
        max_num = value
        index_max = index
    else:
        index_max = array.index(max_num)
    if value < min_num:
        min_num = value
        index_min = index
    else:
        index_min = array.index(min_num)
print(f'Максимальное число: {max_num}, его индекс: {index_max}')
print(f'Минимальное число: {min_num}, его индекс: {index_min}\n')


def get_sum(first_num, second_num):
    result = 0
    for i in array[first_num + 1:second_num]:
        result += i
    return result


if index_min < index_max:
    sum_values = get_sum(index_min, index_max)
else:
    sum_values = get_sum(index_max, index_min)

print(f'Сумма элементов между min и max: {sum_values}')
