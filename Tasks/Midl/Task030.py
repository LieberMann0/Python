# Показать кубы чисел, заканчивающихся на четную цифру

ran = range(2, 30)
for i in ran:
    CubeNum = i ** 3
    if (CubeNum % 10 == 0):
        continue
    elif (CubeNum % 2 == 0):
        print(CubeNum)