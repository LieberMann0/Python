# По двум заданным числам проверять является ли одно квадратом другого

from random import randint
from cmath import sqrt


a = randint(2, 9)
print(a)
b = randint(4, 81)
print(b)
if (sqrt(b) == a):
    print(f'Number {b} is the square of {a}')
else:
    print(f'Number {b} is not square of {a}')
