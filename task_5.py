import random

print('Находим максимальный отрицательный элемент в массиве')

SIZE = 8
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

temp_array = []

for i in array:
    if i < 0:
        temp_array.append(i)
max_neg_num = temp_array[0]
for i in temp_array:
    if i > max_neg_num:
        max_neg_num = i

print(f'Массив элементов:\n{array}\nМаксимальный отрицательный элемент: '
      f'{max_neg_num}, его индекс: {array.index(max_neg_num)}')
