# Выяснить, кратно ли число заданному, если нет, вывести остаток.

from random import randint


numDiv = randint(1, 9)
print(numDiv)
Num = randint(1, 100)
print(Num)
if (Num % numDiv == 0):
    print(f'Число {Num} кратно {numDiv}')
else:
    print(f'Число {Num} не кратно {numDiv} остаток {Num % numDiv}')