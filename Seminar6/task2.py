# 41. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +, -, /, *.
# приоритет операций стандартный. *Пример: * 2 + 2 = > 4;
# 1 + 2 * 3 = > 7;
# 1 - 2 * 3 = > -5;
# - Добавьте возможность использования скобок, меняющих приоритет операций. *Пример: *
# 1 + 2 * 3 = > 7;
# (1 + 2) * 3 = > 9;



# 43. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности. *Пример: *
# [1, 2, 3, 5, 1, 5, 3, 10] = > [2, 10]

symbol = {}
result = 0
str =''
str = input('Введите строку с формулой: ').split()
i = 0
while len(str) != 1:
    if str[i] == '*':
        index = str.index('*')
        str[index] = int(str[index-1]) * int(str[index+1])
        str.remove(str[index-1])
        str.remove(str[index])
        i = 0
        #print(str)
    elif str[i] == '/':
        index = str.index('/')
        str[index] = int(str[index - 1]) / int(str[index + 1])
        str.remove(str[index - 1])
        str.remove(str[index])
        i = 0
        #print(str)
    i += 1

print(str)