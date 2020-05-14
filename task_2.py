# https://drive.google.com/file/d/1aU-6NinHVEz-NfibUl6QUmAmk9XjVrag/view?usp=sharing

print("Побитовые операции И, ИЛИ, исключающее ИЛИ над числами 5, 6")
byte_and = 5 & 6
byte_or = 5 | 6
byte_or_not = 5 ^ 6
print(f'Побитовое И: {byte_and}\nПобитовое ИЛИ: {byte_or}\nИсключающее ИЛИ: {byte_or_not}\n')

print('Побитовый сдвиг числа 5 вправо и влево на два знака')
bmove_right = 5 >> 2
bmove_left = 5 << 2
print(f'Сдвиг вправо: {bmove_right}\nСдвиг влево: {bmove_left}')
