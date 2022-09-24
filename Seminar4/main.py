# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.
# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:

#     1) с помощью математических формул нахождения корней квадратного уравнения

#     2) с помощью дополнительных библиотек Python

# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.


# some_list = [int(i) for i in input().split(' ')]

# print(min(some_list), max(some_list))

# import math

# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))

# D = b**2-4*a*c
# print(D)

# if D < 0:
#     print('Корней нет')
# elif D == 0:
#     x = -b/2*a
#     print(x)
# else:
#     x1 = (-b+math.sqrt(D))/(2*a)
#     x2 = (-b-math.sqrt(D))/(2*a)
#     print(round(x1, 2), round(x2, 2))

import sympy as sm
from sympy import *

result = lcm(int(input('a =')), int(input('b =')))
print(result)

x = sm.Symbol('x')
a = int(input())
b = int(input())
c = int(input())
print(sm.solveset(a * x ** 2 + b * x + c, x))
