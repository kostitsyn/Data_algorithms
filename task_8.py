print('Вычисление суммы каждой строки матрицы')
matr = []
ROWS = 5
COLUMNS = 3

print(f'Введите {ROWS} строк')
for i in range(1, ROWS + 1):
    array = list(map(int, (input(f'{i} строка: введите {COLUMNS} числа через пробел: ')).split()))
    matr.append(array)

for i in matr:
    sum_row = 0
    for elem in i:
        sum_row += elem
        print(f'{elem:>4}', end='')
    print(f'{sum_row:>4}')
