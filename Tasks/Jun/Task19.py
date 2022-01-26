# Определить номер четверти плоскости, в которой находится
# точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0

from random import randint


x = randint(-5, 5)
while x == 0:
    x = randint(-5, 5)
print(f'x = {x}')

y = randint(-5, 5)
while y == 0:
    randint(-5, 5)
print(f'y = {y}')

if ((x) > 0 and (y) > 0):
    print('First quarter')
elif ((x) > 0 and (y) < 0):
    print('Second quarter')
elif ((x) < 0 and (y) < 0):
    print('Third quarter')
elif ((x) < 0 and (y) > 0):
    print('Fourth quarter')