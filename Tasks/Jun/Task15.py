# Дано число. Проверить кратно ли оно 7 и 23

from random import randint


n = randint(23, 700)
print(n)
if ((n % 7 == 0) and (n % 23 == 0)):
    print(f'Number {n} multiple 7 and 23')
elif ((n % 7 == 0) and (n % 23 != 0)):
    print(f'Number {n} multiple 7 only')
elif ((n % 7 != 0) and (n % 23 == 0)):
    print(f'Number {n} multiple 23 only')
elif ((n % 7 != 0) and (n % 23 != 0)):
    print(f'Number {n} not multiple  7 and 23')