import math

# 1. Найти факториал числа 3
factorial_3 = lambda: math.factorial(3)

# 2. Найти факториал числа 5
factorial_5 = lambda: math.factorial(5)

# 3. Найти факториал числа N
factorial_n = lambda n: math.factorial(n)

# 4. Найти факториал числа, пока не введут 0
factorial_until_zero = lambda: [print(f"Факториал {x} = {math.factorial(x)}") for x in iter(lambda: int(input("Введите число (0 для выхода): ")), 0)]