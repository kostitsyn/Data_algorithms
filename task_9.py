# https://drive.google.com/file/d/1aU-6NinHVEz-NfibUl6QUmAmk9XjVrag/view?usp=sharing

print('Введите три разных числа')
num_1 = int(input('Первое число: '))
num_2 = int(input('Второе число: '))
num_3 = int(input('Третье число: '))

if num_1 > num_2:
    if num_1 > num_3:
        if num_2 > num_3:
            print(f'{num_2} - среднее число')
        else:
            print(f'{num_3} - среднее число')
    else:
        print(f'{num_1} - среднее число')
else:
    if num_1 > num_3:
        print(f'{num_1} - среднее число')
    else:
        if num_2 > num_3:
            print(f'{num_3} - среднее число')
        else:
            print(f'{num_2} - среднее число')
