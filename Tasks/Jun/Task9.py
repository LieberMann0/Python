# Показать последнюю цифру трёхзначного числа

ThreeDigitNum = int(input('Enter a three-digit number: '))
while ((ThreeDigitNum // 100) == 0 or (ThreeDigitNum // 100) > 9):
    ThreeDigitNum = int(input('Enter a positive THREE-DIGIT number please: '))
print(ThreeDigitNum % 10)