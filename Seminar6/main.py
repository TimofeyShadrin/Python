# Задача HARD SORT.
# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры.
# Отсортировать элементы по возрастанию слева направо и сверху вниз.
#
# Например, задан массив:
# 1 4 7 2
# 5 9 10 3
#
# После сортировки
# 1 2 3 4
# 5 7 9 10
import random




# m = int(input('Введите количество столбцов: '))
# n = int(input('Введите количество строк: '))
#
# matrix = [
#     [random.randint(0, 10) for _ in range(1, m + 1)]
#     for y in range(1, n + 1)
# ]
#
# print(matrix)
#
# def sort():
#     global matrix
#     new_lst = [i for sublist in matrix for i in sublist]
#     new_lst.sort()
#     matrix = [new_lst[i] ]
#     print(new_lst)
#
# sort()
#
# some_lst = []
# sub_list = []
# for i in range(len(new_lst)):
#     for j in range(len(new_lst) // 3):
#         sub_list.append(new_lst[j])
#     some_lst.append(sub_list)
#     sub_list.clear()
#     i = j

# задача 2 HARD необязательная.
# Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры).
# Вывести на экран красивенько таблицей. Перемешать случайным образом элементы массива,
# причем чтобы каждый гарантированно один раз переместился на другое место и потом не участвовал никак
# (возможно для этого удобно будет использование множества) и выполнить это за m*n / 2 итераций.
# То есть если массив три на четыре, то надо выполнить не более 6 итераций. И далее в конце опять вывести на экран как таблицу.

# m = int(input('Введите количество столбцов: '))
# n = int(input('Введите количество строк: '))
#
# matrix = [
#     [random.randint(0, 9) for _ in range(1, m + 1)]
#     for y in range(1, n + 1)]
#
# for i in range(n):
#     print(*matrix[i], end='\n')
#
# indexes = []
#
# while len(indexes) != m*n - 1:
#     indexes.append(random.randint(0, m*n - 1))
#     indexes = list(set(indexes))
#
# print(indexes)

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

from random import randint
from random import choice

n = int(input("Insert n: "))
m = int(input("Insert m: "))

initList = []
tempList = []

for i in range(n):
    sp = []
    for j in range(m):
        sp.append(randint(-10, 10))
        tempList.append(sp[j])
    initList.append(sp)
print(initList)
print(tempList)
indexList = [0] * m*n
for i in range(m*n):
    indexList[i] = i

for i in range(int(m*n/2)):
    a = choice(indexList)
    indexList.remove(a)
    b = choice(indexList)
    indexList.remove(b)
    tempList[a], tempList[b] = tempList[b], tempList[a]
resultList = []
print(tempList)
for i in range(n):
    sp = []
    for j in range(m):
        sp.append(tempList[0])
        tempList.remove(tempList[0])
    resultList.append(sp)

print(resultList)
