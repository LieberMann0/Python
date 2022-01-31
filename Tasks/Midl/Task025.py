# Найти сумму чисел от 1 до А

from random import randint


a = randint(1, 100)
numbers = range(1, a)
n = len(numbers)
s = 0
for i in numbers:
    s += i

print(f'Sum of numbers from 1 to {n} - {s}')