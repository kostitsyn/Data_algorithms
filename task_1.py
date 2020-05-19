# https://drive.google.com/file/d/1AlBQXW-yjm-D_PB9pQcTtHXLJWGAvmDZ/view?usp=sharing

print('Программа калькулятор для выполнения операций сложения, вычитания, деления, умножения')

while True:
    print('Введите два числа')
    first_num = float(input('Первое число: '))
    second_num = float(input('Второе число: '))
    while True:
        symbol = input('Введите символ знака операции: ')
        if symbol == '+' or symbol == '-' or symbol == '*' or symbol == '/' or symbol == '0':
            break
        else:
            print('Ошибка, введите заново символ')
    if symbol == '0':
        print('Завершение работы программы')
        break
    else:
        if symbol == '/':
            if second_num == 0:
                try:
                    result = first_num / second_num
                except:
                    print('Ошибка, на ноль делить нельзя!')
                    break
            else:
                result = first_num / second_num
        if symbol == '+':
            result = first_num + second_num
        elif symbol == '-':
            result = first_num - second_num
        elif symbol == '*':
            result = first_num * second_num
        elif symbol == '+':
            result = first_num + second_num
        print(f'Результат операции: {result}')
