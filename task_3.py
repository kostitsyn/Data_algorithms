# https://drive.google.com/file/d/1AlBQXW-yjm-D_PB9pQcTtHXLJWGAvmDZ/view?usp=sharing

print('Скрипт переворачивающий натуральное целое число наоборот')

num = int(input('Введите натуральное число: '))
edit_num = int((str(num).rstrip('0')))


def invert(x):
    if 1 <= x and x <= 9:
        return f'{x}'
    return f'{x % 10}{invert((x - x % 10) // 10)}'


print(f'Перевернутое число для {num} будет {invert(edit_num)}')
