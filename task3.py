string = str(input("Введите строку: "))     # вводим строку
if string.count(',') != 0:                  # проверка на наличие запятых в строке
    string = string.replace(',', '')        # можно, если надо, добавить проверку на другие спец. символы

print(string)

words = string.split()

max_length_num = 0                          # длинна самого слова
max_string = ''                             # самое длинное слово

most_common = ''                            # самое частое слово
count_most_meet = 0                         # количество самых частых слов

count_max_meet = 0                          # максимальное количество самых частых слов

for word in words:
    if max_length_num < len(word):          # поиск самого длинного слова
        max_length_num = len(word)
        max_string = word

    for word_popular in words:              # в этом цикле мы считаем сколько раз в тексте встретилось слово
        if word == word_popular:
            count_most_meet += 1

    if count_most_meet > count_max_meet:    # сравниваем с текущим максимальным количеством,
        most_common = word                  # если новое количество больше, то меняем местами
        count_max_meet = count_most_meet

    count_most_meet = 0                     # обнуляем наше количество, для следующего слова

print(f"Самое длинное слово: {max_string}. -> Его длинна равна: {max_length_num}.")
print(f"Наиболее часто встречающееся слово: {most_common}. -> Всего таких слов: {count_max_meet}.")
