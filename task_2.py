import random

print('Скрипт сохраняющий в массиве индексы с чётными элементами исходного массива\n')

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
result_array = []

for index, value in enumerate(array):
    if value % 2 == 0:
        result_array.append(index)
print(f'Исходный массив:\n{array}\n\nИндексы чётных элементов исходного массива:\n{result_array}')
