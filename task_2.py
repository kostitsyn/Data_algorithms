from collections import deque, Counter

print('Скрипт выполняющий сложение двух шестнадцатиричных чисел')

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
    min_len = len(first_num)
    max_len = len(second_num)
    min_num = first_num
    max_num = second_num
else:
    min_len = len(second_num)
    max_len = len(first_num)
    min_num = second_num
    max_num = first_num

for i in range(min_len):
    term_1 = first_num.popleft()
    term_2 = second_num.popleft()
    if i == 0:
        if relation_dict[term_1] + relation_dict[term_2] > DISCHARGE:
            num = relation_dict[term_1] + relation_dict[term_2] - DISCHARGE - 1
            adder = 1
        else:
            num = relation_dict[term_1] + relation_dict[term_2]
            adder = 0
    else:
        if relation_dict[term_1] + relation_dict[term_2] + adder > DISCHARGE:
            num = relation_dict[term_1] + relation_dict[term_2] - DISCHARGE - 1 + adder
            adder = 1
        else:
            num = relation_dict[term_1] + relation_dict[term_2] + adder
            adder = 0
    result.append(reverse_dict[num])
    if i == min_len - 1 and relation_dict[term_1] + relation_dict[term_2] + adder > DISCHARGE:
        adder = 1
        if max_len - min_len == 0:
            result.append(str(adder))

for i in range(len(min_num)):
    max_num.popleft()

for i in range(len(min_num), len(max_num)):
    if i == len(min_num):
        num = relation_dict[max_num.popleft()] + adder
        num = reverse_dict[num]
    else:
        num = relation_dict[max_num.popleft()]
        num = reverse_dict[num]
    result.append(num)
result.reverse()
print(f'Результат суммы: {"".join(result)}')
