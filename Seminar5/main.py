# products = ['iPad', 'Samsung Galaxy', 'iPhone', 'iRiver']
# result = list(filter(lambda x: x.startswith('i'), products))
# print(result)

prices = ['1578.4', '892.4', '354.1', '871.5']
result = tuple(map(float, prices))
print(result)

DISCOUNT = 7
prices = ['1578.4', '892.4', '354.1', '871.5']
result = list(map(lambda x: round((float(x)*DISCOUNT/100), 2), prices))
print(result)
