# https://drive.google.com/file/d/1aU-6NinHVEz-NfibUl6QUmAmk9XjVrag/view?usp=sharing

year = int(input('Введите год: '))

if year % 4 == 0 and year % 100 != 0 or year % 100 == 0 and year % 400 == 0:
    print('Год являтся високосным')
else:
    print('Год не високосный')
