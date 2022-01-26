# Даны два числа. Показать большее и меньшее число

number1 = int(input('Введите первое число - '))
number2 = int(input('Введите второе число - '))
if number1 < number2:
    print(f'Наибольшее число - {number2}')
    print(f'Наименьшее число - {number1}')
else:
    print(f'Наибольшее число - {number1}')
    print(f'Наименьшее число - {number2}')