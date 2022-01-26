# Найти третью цифру числа или сообщить, что её нет

Num = list(input('Enter number: '))
l = len(Num)

if (l <= 2):
    print(f'In this number no third digit')
else:
    print(f'Third digit - {Num[2]}')