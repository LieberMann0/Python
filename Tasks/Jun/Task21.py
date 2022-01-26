# Программа проверяет пятизначное число на палиндром.


FiveDigitN = int(input('Enter five-digit number - '))
while(((FiveDigitN // 100) < 100) or ((FiveDigitN // 100) > 999)):
    FiveDigitN = int(input('Enter FIVE-DIGIT number -'))

FiveDigitList = str(FiveDigitN)

if(((FiveDigitList[0]) == (FiveDigitList[4])) and ((FiveDigitList[1]) == (FiveDigitList[3]))):
    print(f'{FiveDigitN} ПАЛИНДРОМ')
else:
    print(f'{FiveDigitN} не палиндром')
