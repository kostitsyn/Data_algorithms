import random

print('Найти в массиве два наименьших элемента')

SIZE = 8
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

first_min_value = array[0]

print(array)
for i in array:
    if i < first_min_value:
        first_min_value = i
print(f'Первый наименьший элемент: {first_min_value}')

if array.index(first_min_value) == 0:
    second_min_value = array[0 + 1]
else:
    second_min_value = array[0]
for i, j in enumerate(array):
    if j < second_min_value and i != array.index(first_min_value):
        second_min_value = j
print(f'Второй наименьший элемент: {second_min_value}')
