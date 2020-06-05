from random import uniform

print('Сортировка массива методом слияния')

LENGTH = 10
MIN_VALUE = 0
MAX_VALUE = 49
array = [round(uniform(MIN_VALUE, MAX_VALUE), 2) for i in range(LENGTH)]
print(f'Исходный массив: {array}')


def sort_func(first, second):
    result = []
    l_index = 0
    r_index = 0

    while l_index < len(first) and r_index < len(second):
        if first[l_index] <= second[r_index]:
            result.append(first[l_index])
            l_index += 1
        else:
            result.append(second[r_index])
            r_index += 1
    while l_index < len(first):
        result.append(first[l_index])
        l_index += 1
    while r_index < len(second):
        result.append(second[r_index])
        r_index += 1
    return result


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    middle = len(arr) // 2
    l_part = merge_sort(arr[:middle])
    r_part = merge_sort(arr[middle:])
    return sort_func(l_part, r_part)


print(f'Отсортированный массив: {merge_sort(array)}')
