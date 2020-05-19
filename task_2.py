# https://drive.google.com/file/d/1AlBQXW-yjm-D_PB9pQcTtHXLJWGAvmDZ/view?usp=sharing

print('Скрипт для подсчёта чётных и нечётных цифр натурального числа')

number = int(input('Введите натуральное число: '))
even = 0
not_even = 0
DIVIDER = 10
while True:
    digit = number % DIVIDER
    number = (number - digit) // DIVIDER
    if digit % 2 == 0:
        even += 1
    else:
        not_even += 1
    if number == 0:
        break
print(f'Количество чётных чисел: {even}\nКоличество нечётных чисел: {not_even}')
