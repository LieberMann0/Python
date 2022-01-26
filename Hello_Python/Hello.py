# Типы данных и переменные
# int, float, boolean, str, list, None

value = None
print(type(value))

a = 123
b = 1.23

print(a)
print(type(a))

print(b)
print(type(b))


value = 12334
print(value)
print(type(value))

s = 'Hello World'
print(s)    # вывод строки
print(type(s))

# Способы вывода строки
print(a, '-', b, '-', s)
print('{} - {} - {}'.format(a, b, s))
print('{1} - {2} - {0}'.format(a, b, s))
print(f'{a} - {b} - {s}')

f = False
t = True
print(f)
print(type(f))
print(t)
print(type(t))

# Списки (массивы)
l = []
print(l)
print(type(l))

list1 = [1, 2, 3]
print(list1)

list2 = ['1', '2', '3', 'Hello']
print(list2)

list3 = [1.2, 2.3, 3.4]
print(list3)

# Ввод и вывод данных
# print() вывод данных
# input() ввод данных
print('Введите а')
a = input()
print('Введите b')
b = input()
print(a, b)
print('{} {}'.format(a, b))
print(f'{a} {b}')

# если нужно произвести действия:
# с целыми числами
print('Введите а')
a = int(input())
print('Введите b')
b = int(input())
print(a, '+', b, '+', a+b)

# с вещественными числами
print('Введите а')
a = float(input())
print('Введите b')
b = float(input())
print(a, '+', b, '+', a+b)

# Арифметические операции
a = 12
b = 8
c = a + b # сложение

c = a - b # вычетание

c = a * b # умножение

c = a / b # деление дает вещественное число

c = a // b # дает целое число от деления

c = a % b # дает остаток от деления

c = a ** b # возведение в степень

# в случае если:
a = 1.3
b = 3
c = a * b # будет результат вида 3.9000000000000004 (особенность хранения вещественных чисел)
с = round(a * b) # результат будет вида 4 (округлен по математическтм правилам)
с = round(a * b, 3) # число 3 установит количество знаков выводимых после запятой

# сокращенные операции присваивания
a = 3
a = a + 5
a += 5 # сокращенно
# аналогично и для других операций

# Логические операции
# >, <, >=, <=, ==, !=,
# not, and, or - не путать с &, |, ^,
# is, is not, in, not in
# gen

a = 1 > 4
print(a) # False

a = 1 < 4
print(a) # True

a = 1 < 4 < 5 < 10
print(a) # True

a = 1 == 2
print(a) 

a = 1 != 2
print(a) # True

a = 'qwe'
b = 'qwe'
print(a == b) # True

a = [1, 2]
b = [1, 2]
print(a == b) # True

func = 1
T = 4
x = 123
print(func < T < x) # True
print(func < T > x) # False

f = 1 < 4 and 5 > 2
print(f) # True

f = 1 > 4 or 5 > 2
print(f) # True

f = [1, 2, 3, 4]
print(f)
print(2 in f) # True (2 содержится в f)
print(not 2 in f) # False
IsOdd = f[2] % 2 == 0
# то же выражение записать иначе
IsOdd = not f[2] % 2 # отрицание 1 - (True) это есть 0 - (False)
print(IsOdd) # False

# Управляющие конструкции:
# if, if - else
a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a)
else:
    print(b)


username = input('Введите имя: ')
if username == 'Маша':
    print('Ура, ура, это же МАША!')
elif username == 'Марина':
    print('Я так ждал тебя, Марина!')
elif username == 'Борис':
    print('Шалом, Боря!')
else:
    print('Привет, ', username)

# Циклы while
original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print(inverted)

original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Пожалуй')
    print('хватит')
print(inverted)

# Управляющие конструкции for
for i in 1,2,3,4,5:
    print(i**2) # выводит квадрат всех i

list = [1,6,3,8,5]
for i in list:
    print(i) # выводит все элементы list

r = range(10) # набор от 0 до 9
for i in r:
    print(i) # выводит все элементы range

for i in range(5, 10):
    print(i) # выводит все от 5 до 10

for i in range(1, 10, 2): # набор от 1 до 10 с приращением 2
    print(i) # выводит 1, 3, 5, 7, 9

for i in 'qwerty':
    print(i) # выводит побуквенную разбивку

# Строки
text = 'съешь еще этих мягких французских булок'
print(len(text)) # 39
print('еще' in text) # True
print(text.isdigit()) # False
print(text.islower()) # True
print(text.replace('еще', 'ЕЩЕ')) # заменить "еще" на "ЕЩЕ"
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # print(text) по умолчанию [0:len(text)-1]
print(text[:2]) # съ по умолчанию [0:2]
print(text[len(text)-2:]) # ок [len(text)-2:len(text)-1] по умолчанию
print(text[2:9]) # ешь еще
print(text[6:-18]) # еще этих мягких
print(text[0:len(text):6]) # сеикакл - каждая шестая буква текста
print(text[::6]) # сеикакл - каждая шестая буква текста
text = text[2:9] + text[-5] + text[:2] # ...

# Списки
numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]

ran = range(1, 6)
numbers = list(ran) # приведение range к списку (list)
print(numbers) # [1, 2, 3, 4, 5]

numbers[0] = 10
print(numbers) # [10, 2, 3, 4, 5]
print(len(numbers)) # 5

for i in numbers:
    i *= 2
    print(i) # [20, 4, 6, 8, 10]
    print(numbers) # [10, 2, 3, 4, 5]

colors = ['red', 'green', 'blue']
for e in colors:
    print(e) # red green blue

for e in colors:
    print(e*2) # redred greengreen blueblue
colors.append('gray') # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') # del colors[0] # удалить элемент

# Функции
def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return
