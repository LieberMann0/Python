# Задать номер четверти, показать диапазоны для возможных координат

NumQuart = int(input('Enter number of quarter (1 -4): '))
while((NumQuart < 1) or (NumQuart > 4)):
    NumQuart = int(input('Enter number of quarter (1 -4): '))

if(NumQuart == 1):
    print('Coordinates within (+x, +y)')
if(NumQuart == 2):
    print('Coordinates within (+x, -y)')
if(NumQuart == 3):
    print('Coordinates within (-x, -y)')
if(NumQuart == 4):
    print('Coordinates within (-x, +y)')