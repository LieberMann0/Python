# Подсчитать сумму цифр в числе

def SumOfNumbers(a):
    s = str(a)
    sum = 0
    for i in s:
        sum += int(i)        
    return sum


def SumOfNumbers_2(a):
    n = a
    sum = 0
    while (n != 0):
        sum += n % 10
        n //= 10
    return sum
