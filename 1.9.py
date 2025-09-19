non_letters = {'digits': '0123456789', 'symbols': '!@#$%^&*()_+-=[]{}|;:,.<>?/', 'whitespace': ' \t\n\r',
               'other': '"\'\\'}

if __name__ == "__main__":
    char = input("Введите символ: ")
    all_non_letters = ''.join(non_letters.values())

    print(f"Цифра: {char in non_letters['digits']}")
    print(f"Буква: {char not in all_non_letters}")
    print(f"Гласная: {char.lower() in 'aeiouаеёиоуыэюя' and char not in all_non_letters}")
    print(f"Прописная: {char.isupper() and char not in all_non_letters}")