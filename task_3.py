import random

print('Меняем местами минимальный и максимальный элементы массива.')

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

array[index_max], array[index_min] = array[index_min], array[index_max]

print(f'Результирующий список:\n{array}')
