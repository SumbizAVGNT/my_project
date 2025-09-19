numbers = input("Введите 2 числа через пробел: ").split()

if len(numbers) != 2:
    print("Ошибка: нужно ввести ровно 2 числа!")
else:
        num1 = int(numbers[0])
        num2 = int(numbers[1])
        maximum = max(num1, num2)
        minimum = min(num1, num2)

        print("Максимальный вводимый элемент:", maximum)
        print("Минимальный вводимый элемент:", minimum)
        print("Разница между числами:", abs(maximum - minimum))

        if num1 == num2:
            print("Числа равны")
        else:
            print("Числа различны")
