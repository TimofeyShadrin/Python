# print(sum([int(i) for i in input() if i != '.']))  # compression function

import time

print(str(time.time()).split('.')[-1])
a = int(str(time.time()).split('.')[-1])
start = 50
end = 1000
print(a % (end - start) + start)

lst = []
for i in range(5):
    lst.append(input(f'{i} = '))

print(lst)

for el in lst:

    if el.isdigit():
        print("is full digit")
    else:
        for i in el:
            if i.isdigit():
                print("number is in string")
                break
            else:
                continue
        print("no")

some_list = [input() for _ in range(int(input('Введите кол-во элементов: ')))]
n = int(input('Введите число: '))
if str(n) in some_list:
    print('Да')
else:
    print('Нет')

some_list = [input() for _ in range(int(input('Введите кол-во элементов: ')))]
some_str = input('Введите строку: ')
try:
    print(some_list.index(some_str, some_list.index(some_str) + 1))
except:
    print(-1)
