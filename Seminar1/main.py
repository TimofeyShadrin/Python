# # 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

# #     *Примеры:*

# #     - 5, 25 -> да
# #     - 4, 16 -> да
# #     - 25, 5 -> да
# #     - 8,9 -> нет

# # a = int(input('Введите первое число: '))
# # b = int(input('Введите первое число: '))
# # if a**2 == b or b**2 == a:
# #     print('Да')
# # else:
# #     print('Нет')

# a = int(input('Input digit: '))

# for i in range(-a, a + 1):
#     print(i, end=' ')
# text = []
# text = input('Input number: ').split(',')
# number = text[1]

# if len(number) >= 1:
#     print(number[0])
# else:
#     print('None')

# a = int(input('Input digit: '))
# if (a % 5 == 0 and a % 10 == 0 or a % 15 == 0) and a % 30 != 0:
#     print('Кратно 5 и 10 или 15, но не 30')
# else:
#     print('None')

# number = float(input())
# if number // 1 == number:
#     print('нет')
# else:
#     print(int((number * 10 // 1 % 10)))

# number = float(input())
# if number // 1 == number:
#     print('нет')
# else:
#     print(int((number * 10 % 10)))
