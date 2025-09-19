def print_multiplication_table(number, limit=10):
    print(f"\nТаблица умножения на {number}:")
    for i in range(1, limit + 1):
        print(f"{number} × {i} = {number * i}")


def main():
    try:
        # Таблица умножения на 2
        print_multiplication_table(2)

        # Таблица умножения на 5
        print_multiplication_table(5)

        # Таблица умножения на число от пользователя
        user_number = int(input("\nВведите число для таблицы умножения: "))
        print_multiplication_table(user_number)

        # Таблица умножения на 10
        print_multiplication_table(10)

    except ValueError:
        print("Ошибка: введите целое число")


if __name__ == "__main__":
    main()