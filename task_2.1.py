from collections import deque, Counter

print('Скрипт выполняющий умножение двух шестнадцатиричных чисел')

DISCHARGE = 15

first_num, second_num = input('Введите два шестнадцатиричных числа через пробел: ').split()

relation_dict = Counter()
for i in range(10):
    relation_dict[str(i)] = i

for i, j in enumerate(range(ord('A'), ord('F') + 1), 10):
    relation_dict[chr(j)] = i

reverse_dict = Counter()
for i, j in relation_dict.items():
    reverse_dict[j] = i

first_num = deque(first_num)
second_num = deque(second_num)
first_num.reverse()
second_num.reverse()

result = deque()

if len(first_num) < len(second_num):
    min_num = first_num
    max_num = second_num
else:
    min_num = second_num
    max_num = first_num

multip = deque()
for i in min_num:
    adder = 0
    lst = deque()

    for j in max_num:
        res = relation_dict[i] * relation_dict[j] + adder
        if res > 15:
            b = res
            res = res % 16
            adder = b // 16
        else:
            adder = 0
        lst.append(res)

    lst.append(adder)
    multip.append(lst)

print(f'Полученный список: {multip}')

for i in range(len(multip)):
    k = i
    while k != 0:
        multip[i].appendleft(0)
        k -= 1

y = deque(map(len, multip))
max_len = max(y)

for i in multip:
    if len(i) == max_len:
        continue
    if len(i) < max_len:
        j = len(i)
        while j != max_len:
            i.append(0)
            j += 1

temp_array = deque()
sum_ = 0
for i in range(len(multip[0])):
    sum_ = 0
    for j in range(len(multip)):
        sum_ += multip[j][i]
    result.append(sum_)

hg = deque()
c = 0

for i in result:
    i = i + c
    if i > 15:
        b = i
        i = i % 16
        c = b // 16
    else:
        c = 0
    hg.append(reverse_dict[i])
hg.reverse()
print(f'Результат умножения: {"".join(hg)}')
