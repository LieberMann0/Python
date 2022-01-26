# Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y

x = 'x'
y = 'y'
print((not (x or y)) == (not (x) and not (y))) # True
