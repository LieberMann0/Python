# Показать таблицу квадратов чисел от 1 до N

from random import randint


n = randint(1, 25)
a = range(1, n)
for i in a:
    print(f'Square of number {i} - {i**2}')