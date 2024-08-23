def main(input_str: str) -> str:
    try:
        parts = input_str.strip().split()

        if len(parts) != 3:
            raise ValueError("Неправильный формат ввода. Ожидалось два числа и один оператор.")

        a_str, operator, b_str = parts

        a = int(a_str)
        b = int(b_str)

        if not (1 <= a <= 10 and 1 <= b <= 10):
            raise ValueError("Числа должны быть от 1 до 10 включительно.")

        if operator == '+':
            result = a + b
        elif operator == '-':
            result = a - b
        elif operator == '*':
            result = a * b
        elif operator == '/':
            if b == 0:
                raise ZeroDivisionError("Деление на ноль невозможно.")
            result = a // b
        else:
            raise ValueError("Недопустимый оператор. Допустимые операторы: +, -, *, /.")

        return str(result)

    except ValueError as e:
        raise Exception(f"Ошибка: {e}")
    except ZeroDivisionError as e:
        raise Exception(f"Ошибка: {e}")

if __name__ == "__main__":
    while True:
        try:
            user_input = input("Введите выражение (например, '2 + 3'): ")
            output = main(user_input)
            print(f"Результат: {output}")
        except Exception as e:
            print(e)
            break
