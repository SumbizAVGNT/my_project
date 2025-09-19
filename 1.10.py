# Полный функциональный подход с iter() и sentinel
if __name__ == "__main__":
    # 1. Сумма до 0
    numbers1 = []
    for num in iter(lambda: int(input("Введите число (0 для выхода): ")), 0):
        numbers1.append(num)
    print(f"1. Сумма: {sum(numbers1)}")

    # 2. Количество до отрицательного
    numbers2 = []
    for num in iter(lambda: int(input("Введите число (отрицательное для выхода): ")), -1):
        if num < 0:
            break
        numbers2.append(num)
    print(f"2. Количество: {len(numbers2)}")

    # 3. Сумма нечётных до чётного
    numbers3 = []
    # Используем sentinel None, так как условие сложнее
    for num in iter(lambda: int(input("Введите число (чётное для выхода): ")), None):
        if num % 2 == 0:
            break
        numbers3.append(num)
    print(f"3. Сумма нечётных: {sum(numbers3)}")

    # 4. Среднее до >100
    numbers4 = []
    # Также используем sentinel None для сложного условия
    for num in iter(lambda: int(input("Введите число (>100 для выхода): ")), None):
        if num > 100:
            break
        numbers4.append(num)
    avg = sum(numbers4) / len(numbers4) if numbers4 else 0
    print(f"4. Среднее арифметическое: {avg}")