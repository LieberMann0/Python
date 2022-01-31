# Возведите число А в натуральную степень B используя цикл

def ToDegree(a, b):
    i = 1
    res = a
    while (i < b):
        res *= a
        i += 1
    return res
