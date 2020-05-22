import random

print('Находим максимальный элемент среди минимальных элементов столбцов матрицы')

SIZE_ROWS = 8
SIZE_COLUMNS = 5
MIN_ITEM = 0
MAX_ITEM = 8
matr = [[random.randint(MIN_ITEM, MAX_ITEM) for j in range(SIZE_ROWS)] for i in range(SIZE_COLUMNS)]

print('Матрица:')
for i in matr:
    print(*i)

temp_array = []
for i in range(len(matr[0])):
    min_elem = matr[0][i]
    for j in range(len(matr)):
        if matr[j][i] < min_elem:
            min_elem = matr[j][i]
    temp_array.append(min_elem)

print('Минимальные значения в столбцах: ', end='')
print(*temp_array)

max_elem = temp_array[0]
for i in temp_array:
    if i > max_elem:
        max_elem = i
print(f'Максимальное значение из минимальных значений: {max_elem}')
