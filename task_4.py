# https://drive.google.com/file/d/1AlBQXW-yjm-D_PB9pQcTtHXLJWGAvmDZ/view?usp=sharing

print('Посчитать сумму элементов для ряда чисел 1, -0.5, 0.25, -0.125,...')
n = int(input('Введите натуральное число - количество элементов ряда: '))

for i in range(1, n + 1):
    if i == 1:
        sum_row = 1
    else:
        sum_row += (1 / (-2) ** (i - 1))

print(f'Сумма элементов ряда равна {sum_row}')
