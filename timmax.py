import random

n = int(input('Nhap n :'))
list = random.sample(range(1,15),n)
max = list[0]
for item in list:
    if item > max :
        max = item
print('List = ',list)
print('Max la :',max)