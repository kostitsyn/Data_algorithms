# https://drive.google.com/file/d/1aU-6NinHVEz-NfibUl6QUmAmk9XjVrag/view?usp=sharing

print('Введите длины трёх отрезков')
a = int(input('Первый: '))
b = int(input('Второй: '))
c = int(input('Третий: '))

if a <= 0 or b <= 0 or c <= 0:
    print('Треугольник не может быть получен')
elif a == b and b == c:
    print('Треугольник является равносторонним')
elif a == b or a == c or b == c:
    print('Треугольник является равнобедренным')
else:
    print('Треугольник является разносторонним')
