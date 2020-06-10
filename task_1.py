from hashlib import sha1


def count_substr(string):
    res = []
    for i in range(1, len(string)):
        for j in range(len(string)):
            substr = sha1(string[j:j + i].encode('utf-8')).hexdigest()
            if substr in res:
                continue
            res.append(substr)
    return len(res)


my_string = input('Введите строку: ')
print(f'Количество подстрок в строке {my_string}: {count_substr(my_string)}')
