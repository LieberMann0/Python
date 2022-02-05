# Файлы


#  запись в файл

colors = ['red', 'green', 'blue'] # набор данных
data = open('file.txt', 'a') # создаем текстовую переменную и связываем её с файлом
#('a' - дозапись в файл, 'w' - перезапись содержимого, 'r' - чтение)
data.writelines(colors) # дозапись в файл имеющиеся данные (разделителей не будет)
data.write('\nLINE 2\n') # \n - перевод с новой строки, дозапись LINE 2, \n перевод строки
data.write('LINE 3\n')# дозапись LINE 3, \n перевод строки
data.close() # закрытие файла (не забывать)


#  другой способ написания

colors = ['red', 'green', 'blue']
with open('file.txt', 'a') as data:
    data.write('\nLINE 2\n')
    data.write('LINE 3\n')
    # после завершения команда data.close будет вызвана автоматически


#  чтение из файла

path = 'file.txt'
data = open(path, 'r') # открываем файл в режиме чтения
for line in data:
    print(line)
data.close()



# Функции и модули


# модули

# Чтобы не писать 1000-строчный код, можно заготавливать свой файл (например my_File.py)
# с набором своих функций (к примеру (f), (ToDegree),  итп ) и вызывать их
# как модули из этого файла.

# import my_File.py

# print(ToDegree(a, b))
# print(SumOfNumbers(a))


# свойства функции по умолчанию

def new_string(symbol, count):
    return symbol * count
print(new_string ('!', 5)) # Результатом будет !!!!!
print(new_string ('!')) # Результатом будет ошибка

# а если

def new_string(symbol, count = 3):
    return symbol * count
print(new_string ('!', 5)) # Результатом будет - !!!!!
print(new_string ('!')) # Результатом будет - !!!
print(new_string (4)) # Результатом будет - 12


# возможность передачи функции любого количества аргументов

def concatenatio (*params): # перед аргументом ставится *
    res: str = "" # способ прописывания типа данных (str) для переменной res (не обязательно, но можно и так)
    for item in params:
        res += item
    return res

print(concatenatio('a', 's', 'd', 'w')) # asdw
print(concatenatio('a', '2')) # a2
print(concatenatio(1, 2, 3, 4)) # TypeError (работа идет со строкой)



# Рекурсия


def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

list = []
for e in range(1, 10):
    list.append(fib(e))
    print(list) # Результат - 1 1 2 3 5 8 13 21 34



# Кортежи (неизменяемые списки) tuple


a = (3, 1, 41, 4) # Может состоять из неизменяемых элементов
# a = (3,) - кортеж из одного элемента
print(a) # (3, 1, 41, 4)
print(a[0]) # 3
print(a[-2]) # 41
print(a[-1]) # 4
# a[0] = 12 - TypeError. Как в списке присвоить элементу новое значение нельзя



# Словари


dictionary = {}
dictionary = \
    {
        
    }
print(dictionary) # {'up': '↑', 'left': '←', 'down': '↓', 'right': '→',}
print(dictionary['left']) # ←
#типы ключей могут отличаться

for k in dictionary.keys():
    print(k) # выводится список ключей

for k in  dictionary.values():
    print(k) # выводится список значений

for k in  dictionary:
    print('{}: {}'.format(k, dictionary[k]))
# выводится
# up: ↑ 
# left: ←
# down: ↓
# right: →


dictionary['left'] = '◄'
print(dictionary['left']) # ◄
del dictionary['left'] # удаление элемента



# Множества


colors = {'red', 'green', 'blue'} # - множество
print(colors) # {'red', 'green', 'blue'}

colors.add('red') # добавление элемента, который уже есть
print(colors) # {'red', 'green', 'blue'}
colors.add('gray') # добавление нового элемента
print(colors) # {'red', 'green', 'blue', 'gray'}

colors.remove('red') # удаление элемента
print(colors) # {'green', 'blue', 'gray'}
colors.remove('red') # удаление не существующего элемента - KeyError: 'red'
colors.discard('red') # ok (такое удаление несуществующего элемента ошибкт не вызывает)
print(colors) # {'green', 'blue', 'gray'}

colors.clear() # полностью очищает множество
print(colors) # set()

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8} - создание нового множества на основе имеющегося
u = a.union(b) # u = (1, 2, 3, 5, 8, 13, 21) - создание нового на основе объединения множеств
i = a.intersection(b) # i = {2, 5, 8} - пересечение множеств
dl = a.difference(b) # dl = {1, 3} - разность множеств a-b
dr = b.difference(a) # dr = {13, 21} - разность множеств  b-a

q = a.union(b).difference(a.intersection(b))
print(q)
# иначе записать
q = a \
    .union(b) \
    .difference(a.intersection(b))
print(q)


# неизменяемое маожество

a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b) # frozenset({1, 2, 3, 5, 8})



    