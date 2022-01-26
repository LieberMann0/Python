# Найти максимальное из трех чисел

number1 = int(input('Введите первое число - '))
number2 = int(input('Введите второе число - '))
number3 = int(input('Введите третье число - '))
max = number1
if max < number2:
    max = number2

if max < number3:
    max = number3
print(f'Наибольшее число - {max}')