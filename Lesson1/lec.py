
a = 123
b = 1.23
print(type(a))
print(b)
value = None
s = 'Hello world!'
print(s)  # print(value)
s = 'Hello \"world!\"'
print(s)  # print(value)
print(a, b, s)  # print(a, b, s)
print(a, '-', b, '-', s)  # print(a, b, s
print(f'{a}', b, '-', s)  # print(f'

f = True
print(f)
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # list
print(list)  # print(list)
#a = int(input())
#b = float(input())
1
a = 1.3
b = 3
b += 1
c = round(a*b, 2)
print(c)

a = 1 < 4 and 5 > 4
print(a)  # print
a = 1 < 3 < 5 < 7
print(a)  # print

f = 1 > 2 or 4 < 6
f = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(2 in f)
print(not 11 in f)

is_odd = f[0] % 2 == 0  # четное
is_odd = not f[0] % 2  # нужно нечетное
print(is_odd)

a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a)
    # elif
else:
    print(b)

original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print(inverted)

for i in range(1, 10, 2):  # от 1 до 10 с приращением 2
    print(i)

text = 'привет всем кто здесь есть'
print(len(text))
print('есть' in text)
print(text.isdigit())
print(text.islower())
print(text.replace('есть', 'ЕСТЬ'))

help(text.istitle)

print(text[-5])
print(text[2:9])
numbers = []
for i in range(0, 16, 2):
    numbers.append(i)
print(numbers)
