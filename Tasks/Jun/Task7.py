# Показать числа от -N до N

NegNum = 0
while (NegNum >= 0):
    NegNum = int(input('Enter negative number: '))

PosNum = 0
while (PosNum <= 0):
    PosNum = int(input('Enter positive number: '))

Numb = range(NegNum, (PosNum + 1))
for i in Numb:
    print(i)