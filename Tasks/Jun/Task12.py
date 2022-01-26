# Удалить вторую цифру трёхзначного числа

num = (input('Enter a three-digit number: '))
print(num[::2])

# Вариант2
num2 = (input('Enter a three-digit number: '))
print(f'{num2[0]}{num2[2]}')

# Вариант 3
num3 = int(input('Enter a three-digit number: '))
threedigit = ((num3 // 100) * 10) + (num3 % 10)
print(threedigit)

# Вариант 4(?)