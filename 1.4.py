def sum_odd_numbers(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            total += i
    return total


def sum_1_to_n_formula(n):
    return n * (n + 1) // 2

def sum_even_numbers_formula(n):

    k = n // 2
    return 2 * (k * (k + 1) // 2)

def sum_odd_numbers_formula(n):

    k = (n + 1) // 2
    return k * k


if __name__ == "__main__":



    try:
        N = int(input("\n2. Введите число N: "))


        print(f"   (по формуле): {sum_1_to_n_formula(N)}")

        print(f"   (по формуле): {sum_even_numbers_formula(N)}")

        print(f"4. Сумма нечётных чисел от 1 до {N}: {sum_odd_numbers(N)}")
        print(f"   (по формуле): {sum_odd_numbers_formula(N)}")

    except ValueError:
        print("Ошибка! Пожалуйста, введите целое число.")