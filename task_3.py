from random import randint

print('Найти медиану в неотсортированном массиве')

CONST = 2
MIN_VALUE = 0
MAX_VALUE = 20
array = [randint(MIN_VALUE, MAX_VALUE) for i in range(2 * CONST + 1)]
print(f'Массив элементов: {array}')
half_ar = (len(array) - 1) // 2
for i in array:
    counter = 0
    double = 0
    for j in array:
        if i >= j:
            counter += 1
            if i == j:
                double += 1
    if counter == half_ar + 1:
        mediana = i
        break
    if double > 1:
        mediana = i
print(f'Медиана массива: {mediana}')
