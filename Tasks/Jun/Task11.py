# Дано число из отрезка [10, 99]. Показать наибольшую цифру числа

from random import randint


Num = randint(10, 99)
print(Num)
a = Num // 10
b = Num % 10
if (a > b):
    print(f'The largest number - {a}')
else:
    print(f'The largest number - {b}')