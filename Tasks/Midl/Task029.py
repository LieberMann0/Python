# Написать программу вычисления произведения чисел от 1 до N


def SumOfNumbers(N):
    comp = 1
    for i in range(1, (N + 1)):
        comp *= i
    return comp

# a = N
# print(SumOfNumbers(a))