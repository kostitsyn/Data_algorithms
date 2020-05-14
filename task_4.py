# https://drive.google.com/file/d/1aU-6NinHVEz-NfibUl6QUmAmk9XjVrag/view?usp=sharing

import random

print("Введите границы для случайного целого числа")
min_value = int(input('min: '))
max_value = int(input('max: '))
random_value = random.randint(min_value, max_value)
print(f'Случайное целое число: {random_value}\n')

print("Введите границы для случайного вещественного числа")

min_value = float(input('min: '))
max_value = float(input('max: '))
random_value = round(random.uniform(min_value, max_value), 2)
print(f'Случайное вещественное число: {random_value}\n')

print("Введите нижнее и верхнее значение для диапазона символов")

min_value = input('min: ')
max_value = input('max: ')
random_value = chr(random.randint(ord(min_value), ord(max_value)))
print(f'Случайный символ: {random_value}')
