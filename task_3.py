# https://drive.google.com/file/d/1aU-6NinHVEz-NfibUl6QUmAmk9XjVrag/view?usp=sharing

print('Ввести координаты двух точек')
x1 = int(input('x1: '))
y1 = int(input('y1: '))
x2 = int(input('x2: '))
y2 = int(input('y2: '))
print()
k = round(((y2 - y1) / (x2 - x1)), 2)
b = round((y1 - k * x1), 2)
print(f'y = {k}x + {b}')
