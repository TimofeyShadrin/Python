'''
35. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
'''
# my_str = '1 2 3 4 6 7'
#
# nums = list(map(int, my_str.split()))
#
#
# # print(nums)
#
# def find_num(some_list):
#     for i in range(len(some_list) - 1):
#         if some_list[i + 1] - some_list[i] > 1:
#             return some_list[i] + 1
#
#
# print(find_num(nums))
#
# result = [nums[i - 1] for i in range(1, len(nums)) if nums[i] - 1 != nums[i - 1]]
# print(result)

'''
36. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
Пример:
[1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7]
'''
# nums_list = [1, 5, 2, 3, 4, 6, 1, 7]
# result = [nums_list[0]]
# [result.append(nums_list[i]) for i in range(1, len(nums_list)) if nums_list[i] > result[-1]]
# print(result)


'''
37. Напишите программу, удаляющую из текста все слова, содержащие "абв".
'''

# my_str = 'Напиабвшите программу, удаляабвющую из текста все слова, содержащие "абв"'
#
# my_str = my_str.split(' ')
# res = ''
# for word in my_str:
#     if word.find('абв') == -1:
#         res += word + ' '
#
# print(res)
