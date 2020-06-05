from random import randint

print('Сортировка массива пузырьком по убыванию')

LENGTH = 10
MIN_VALUE = -100
MAX_VALUE = 99
array = [randint(MIN_VALUE, MAX_VALUE) for i in range(LENGTH)]

print(f'Исходный массив: {array}')


def bubble_sort(arr):
    n = 1
    while n < len(arr):
        spam = 0
        for i in range(len(arr) - n):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                spam = 1
        if spam == 0:
            break
        n += 1
    return arr


print(f'Отсортированный массив: {bubble_sort(array)}')
