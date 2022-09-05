# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

# *Пример: *

# - Для N = 5: 1, -3, 9, -27, 81
# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.

# *Пример: *

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

# n = int(input())
# for x in range(n - 1):  # 0,1,2,3,4
#     function = (-3) ** x
#     print(function, end=", ")

# n = int(input('Please enter a number: '))
# for x in range(1, n + 1):  # 0,1,2,3,4
#     function = 3 * x + 1
#     print(f'{x}: {function}')

# s1 = input('Enter fist string: ')
# s2 = input('Enter second string: ')
# print(s1.count(s2))
# print(s2.count(s1))

# n = int(input())
# some_list = []
# for i in range(n):
#     some_list.append((-3) ** i)
# print(*some_list, sep=', ')

# def func(x):
#     return 3 * x + 1

# n = int(input())
# some_dict = {}
# for i in range(1, n + 1):
#     some_dict[i] = func(i)
# print(some_dict)

# str1 = input()
# str2 = input()
# print(str1.lower().count(str2.lower()) or str2.lower().count(str1.lower()))

# str1 = input()
# str2 = input()
# count = 0
# if len(str1) < len(str2):
#     len_str1 = len(str1)
#     i = 0
#     while i < len(str2):
#         if str1[0] == str2[i]:
#             if str1[1:] == str2[i + 1: i + len_str1]:
#                 count += 1
#                 i += len_str1
#             else:
#                 i += 1
#         else:
#             i += 1
# print(count)
