# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

# n = int(input("Введите размер списка: "))
# X = int(input("введите Х: "))

# A = []

# for i in range(n):
#     number = i+1
#     A.append(number)

# print(A)
# count = 0
# for i in range(n):
#     if A[i]==X:
#         count +=1
# print(F"X встречатеся в списке А {count} раз")



# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

# import random
# n = int(input("Введите размер списка: "))
# X = int(input("введите Х который ищем: "))

# numbers = []

# for i in range (n):
#     number = random.randint(0, 100)
#     numbers.append(number)

# print(numbers)
# A = numbers[i]

# for i in numbers:
#     if (i - X)<(A-X):
#         A = i
# print(F"ближайшее число - [{A}]")        




# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. 

# В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.

# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
# Ввод:
# ноутбук
# Вывод:
# 1

string = input("Введите строку: ")
count = 0
for i in string:
    if i.lower() == "а" or i.lower() == "в"or i.lower() == "е"or i.lower() == "и"or i.lower() == "н"or i.lower() == "о"or i.lower() == "р"or i.lower() == "с"or i.lower() == "т":
        count += 1
    if i.lower() == "д"or i.lower() == "к"or i.lower() == "л"or i.lower() == "м"or i.lower() == "п"or i.lower() == "у":
        count += 2
    if i.lower() == "б"or i.lower() == "г"or i.lower() == "ё"or i.lower() == "ь"or i.lower() == "я":
        count += 3
    if i.lower() == "й"or i.lower() == "ы":
        count += 4
    if i.lower() == "ж"or i.lower() == "з"or i.lower() == "х"or i.lower() == "ц"or i.lower() == "ч":
        count += 5
    if i.lower() == "ш"or i.lower() == "э"or i.lower() == "ю":
        count += 8
    if i.lower() == "ф"or i.lower() == "щ"or i.lower() == "ъ":
        count += 10
print(F"количество очков - [{count}]")




string = input("Введите строку: ")
count = 0
points = {'а': 1, 'в': 1, 'е': 1, 'и': 1, 'н': 1, 'о': 1, 'р': 1, 'с': 1, 'т': 1,
          'д': 2, 'к': 2, 'л': 2, 'м': 2, 'п': 2, 'у': 2,
          'б': 3, 'г': 3, 'ё': 3, 'ь': 3, 'я': 3,
          'й': 4, 'ы': 4,
          'ж': 5, 'з': 5, 'х': 5, 'ц': 5, 'ч': 5,
          'ш': 8, 'э': 8, 'ю': 8,
          'ф': 10, 'щ': 10, 'ъ': 10}
for i in string:
    if i.lower() in points:
        count += points[i.lower()]
print(f"количество очков - [{count}]")