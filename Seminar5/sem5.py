# Задача HARD SORT.
# Задайте двумерный массив из целых чисел.
# Количество строк и столбцов задается с клавиатуры.
# Отсортировать элементы по возрастанию слева направо и сверху вниз.
# Например, задан массив:
# 1 4 7 2
# 5 9 10 3
# После сортировки
# 1 2 3 4
# 5 7 9 10
#
# задача 2 HARD необязательная. Сгенерировать массив
# случайных целых чисел размерностью m*n (размерность вводим с клавиатуры).
# Вывести на экран красивенько таблицей.
# Перемешать случайным образом элементы массива, причем чтобы каждый гарантированно один раз переместился на другое место и потом не участвовал никак (возможно для этого удобно будет использование множества) и выполнить это за m*n / 2 итераций. То есть если массив три на четыре, то надо выполнить не более 6 итераций. И далее в конце опять вывести на экран как таблицу.

import random as r


def sort(arr):
    for k in range(len(arr)):
        min = k
        for i in range(k, len(arr)):
            if arr[i] < arr[min]:
                min = i
        arr[min], arr[k] = arr[k], arr[min]

    return arr


def median(arr):
    return arr[(len(arr)) // 2]


rows = int(input('Число строк в массиве '))
column = int(input('Число колонок в массиве '))
matrix = [[r.randint(-10, 10) for i in range(column)] for j in range(rows)]
temp = []


def print_dimentional(matrix):
    for lists in matrix:
        print(lists)
    print()


for i in range(rows):
    for j in range(column):
        temp.append(matrix[i][j])

sorted_temp = sort(temp)

print()
print(f'median {median(sorted_temp)}')

print_dimentional(matrix)

for i in range(rows):
    for j in range(column):
        matrix[i][j] = sorted_temp[i * column + j]

print_dimentional(matrix)
