# https://drive.google.com/file/d/1AlBQXW-yjm-D_PB9pQcTtHXLJWGAvmDZ/view?usp=sharing

print('Вывод пар код - символ таблицы ASCII символов с кодом от 32 до 127 включительно')
first_code_sym = 32
last_code_sym = 127
STEP_ROW = 10
while True:
    for i in range(first_code_sym, last_code_sym + 1):
        if i < first_code_sym + STEP_ROW:
            print(f"{i}-{chr(i)}", end=' ')
    print()
    first_code_sym += STEP_ROW
    if first_code_sym > last_code_sym:
        break
