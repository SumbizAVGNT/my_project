if __name__ == "__main__":
    print("1. Квадрат 7:", (lambda x: x ** 2)(7))
    print("2. Куб 4:", (lambda x: x ** 3)(4))

    n, x = 3, 2
    print(f"3. {x} в степени {n}:", (lambda x, n: x ** n)(x, n))

    n2 = 5
    print(f"4. 2 в степени {n2}:", (lambda n: 2 ** n)(n2))