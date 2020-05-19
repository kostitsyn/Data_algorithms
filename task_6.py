# https://drive.google.com/file/d/1AlBQXW-yjm-D_PB9pQcTtHXLJWGAvmDZ/view?usp=sharing
import random

print('Игра угадайка')

guess_number = random.randint(0, 100)
try_guess = 10
for i in range(try_guess + 1):
    if i == try_guess:
        print('Вы не смогли угадать число')
        break
    else:
        input_number = int(input('Введите целое число от 0 до 100: '))
        if guess_number == input_number:
            print('Вы угадали число!!!')
            break
        elif input_number > guess_number:
            print('Вы ввели слишком большое число')
        else:
            print('Вы ввели слишком маленькое число')
        if i < try_guess - 1:
            print(f'У вас осталось {try_guess - (i + 1)} попыток')
