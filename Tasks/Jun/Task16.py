# Дано число обозначающее день недели. Выяснить является номер дня недели выходным

DaysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
n = int(input('Enter number day of week - '))

while (n < 1 or n > 7):
    n = int(input('Enter number day of week (1 - 7) - '))

if (n == 6 or n == 7):
    print(f'{n}-th day is {DaysOfWeek[n - 1]} - Weekend')
else:
    print(f'{n}-th day is {DaysOfWeek[n - 1]} - Not weekend')