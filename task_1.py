# https://drive.google.com/file/d/1aU-6NinHVEz-NfibUl6QUmAmk9XjVrag/view?usp=sharing

x = int(input('Введите трёхзначное число: '))
c = x % 10
b = (x % 100 - c) // 10
a = (x // 10 - b) // 10

print(f'Сумма цифр введённого числа равна {a + b + c}\nпроизведение цифр равно {a * b * c}')
