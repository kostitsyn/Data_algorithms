from collections import Counter

print('Алгоритм Хаффмана')


def haffman(lst, countr='', f=0):
    for i in lst:
        if isinstance(i, str):
            words_dct[i] += countr * f + str(lst.index(i))
            continue
        a = str(lst.index(i))
        haffman(i, a, f + 1)
    res_str = ''
    for i in my_str:
        res_str += words_dct.get(i)
    return res_str


my_str = input('Введите строку: ')
words_dct = dict()
for i in my_str:
    words_dct[i] = ''

count_words = Counter(my_str)
len_ct = len(count_words)

temp_list = count_words.most_common(len_ct)

temp_list = list(map(list, temp_list))

result = []

for i in range(len(temp_list) - 1):
    l_1 = temp_list[len(temp_list) - 1]
    if i == 0:
        l_2 = temp_list[len(temp_list) - 2]
        summary = l_1[1] + l_2[1]
        spam = [l_1[0], l_2[0]]
        temp_list.pop()
        temp_list.pop()
        result.append(spam)
    else:
        if summary > l_1[1]:
            if i != 1:
                result = [result]
            result.insert(0, l_1[0])
        else:
            result.append(l_1[0])

        summary += l_1[1]
        temp_list.pop()

print(f'Закодированная строка: {haffman(result)}')
