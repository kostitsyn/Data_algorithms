# https://drive.google.com/file/d/1aU-6NinHVEz-NfibUl6QUmAmk9XjVrag/view?usp=sharing

print('Введите две буквы')
first_letter = input('Первая буква: ')
second_letter = input('Вторая буква: ')

ser_first_let = ord(first_letter) - 96
ser_second_let = ord(second_letter) - 96

count_letter = (ser_second_let
                - ser_first_let
                - 1)

print(f'Буква {first_letter} находится в алфавите на позиции {ser_first_let}\n'
      f'Буква {second_letter} находится в алфавите на позиции {ser_second_let}\n'
      f'Количество букв между ними {count_letter}')
