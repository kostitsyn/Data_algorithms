print('Скрипт, подсчитывающий сколько чисел от 2 до 99 кратны каждому из чисел от 2 до 9.')
START_ARRAY = 2
END_ARRAY = 99
START_RANGE = 2
END_RANGE = 9
array = [i for i in range(START_ARRAY, END_ARRAY + 1)]

for i in range(START_RANGE, END_RANGE + 1):
    counter = 0
    for j in array:
        if j % i == 0:
            counter += 1
    print(f'Числу {i} кратно {counter} чисел')
