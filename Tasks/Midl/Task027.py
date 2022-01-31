# Определить количество цифр в числе

def CountingDigits(a):
    res = a
    count = 0
    while (res > 0):
        res = res // 10
        count += 1
    return count


def CountingDigits_2(a):
    s = str(a)
    count = (len(s))
    return count
