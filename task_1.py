from collections import deque, defaultdict

print('Вывести предприятия чья прибыль выше среднего и предприятия, чья прибыль ниже среднего')
QUARTER = 4
num_company = int(input('Введите количество предприятий: '))
dict_company = defaultdict(deque)
for i in range(num_company):
    name_company = input('Введите название предприятия: ')
    for i in range(1, QUARTER + 1):
        profit = int(input(f'Введите прибыль предприятия "{name_company}" за {i}-й квартал: '))
        dict_company[name_company].append(profit)

average = sum(deque(map(sum, dict_company.values()))) // num_company

deq_higher = deque()
deq_below = deque()
for i in dict_company:
    if average < sum(dict_company[i]):
        deq_higher.append(i)
    else:
        deq_below.append(i)
print()
print(f'Средняя прибыль предприятий: {average}\nПредприятия с доходом выше среднего: {", ".join(deq_higher)}\n'
      f'Предприятия с доходом ниже среднего: {", ".join(deq_below)}')
