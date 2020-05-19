# https://drive.google.com/file/d/1AlBQXW-yjm-D_PB9pQcTtHXLJWGAvmDZ/view?usp=sharing

print('Скрипт проверяющий истину выражения 1+2+...+n = n(n+1)/2 ')

def summary(x):
    if x == 1:
        return 1
    return summary(x - 1) + x


num = int(input('Введите натуральное число: '))

left_part = summary(num)
right_part = num * (num + 1) / 2

if left_part == right_part:
    print(f'{left_part}={right_part} - выражение истинно')
else:
    print(f'{left_part}={right_part} - выражение ложно')
