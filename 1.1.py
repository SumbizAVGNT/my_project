def check_number(n):


    is_even = (n % 2) == 0
    divisible_by_5 = n % 5 == 0
    divisible_by_7 = n % 7 == 0
    ends_with_3 = abs(n) % 10 == 3

    return is_even, divisible_by_5, divisible_by_7, ends_with_3



def main():
    try:
        number = int(input("Введите число: "))
        results = check_number(number)
        print(f"Число {number}:")
        print(f"• Чётное: {'да' if results[0] else 'нет'}")
        print(f"• Делится на 5: {'да' if results[1] else 'нет'}")
        print(f"• Делится на 7: {'да' if results[2] else 'нет'}")
        print(f"• Оканчивается на 3: {'да' if results[3] else 'нет'}")

    except ValueError:
        print("Ошибка: введите целое число")


if __name__ == "__main__":
    main()