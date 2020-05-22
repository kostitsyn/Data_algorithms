import random

print('Определяем какое число в массиве встречается чаще всего')

SIZE = 8
MIN_ITEM = 0
MAX_ITEM = 4
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
max_replace = 0
for i in array:
    counter = 0
    for j in array:
        if i == j:
            counter += 1
    if counter > max_replace:
        max_replace = counter
        num = i

print(f'Массив элементов:\n{array}\nЭлемент встречающийся чаще всего: {num}')
