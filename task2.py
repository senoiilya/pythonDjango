string = str(input("Введите строку: "))

count_c = 0
length = len(string)
nw_string = str()

for i in range(length):
    if (i == 2):                                        # пропуск третьего символа
        continue

    if (string[i] == 'с'):
        count_c += 1                                    # подсчёт количества символа 'c'
        print(f"Есть символ 'с'. Он уже {count_c}.")    # вывод информации о нахождении символа

    nw_string += string[i]                               # создание новой строки, без третьего символа

    if (i + 1 == length):                               # вывод строки без последнего символа
        print(nw_string[:-1])

print(f"Длина строки равна = {len(string)}")
