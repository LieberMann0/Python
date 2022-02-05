# Для натурального N создать множество: 1, -3, 9, -27, 81 и т.д.

N = [1]
const = (-3)
res = 1
x = None # Вместо None ввести необходимое магическое число
while (res < x):
    res *= (const)
    N.append(res)
print(N)


# Вариант

N = [1]
const = (-3)
res = 1
x = None # Вместо None ввести необходимое магическое число
for i in range(1, x):
    res *= (const)
    N.append(res)
print(N)