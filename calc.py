def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b

def main():
    print("Простой калькулятор на Python")
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: введите корректное число!")
        return

    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    choice = input("Ваш выбор (1/2/3/4): ")

    try:
        if choice == '1':
            result = add(num1, num2)
            operation = "сложения"
        elif choice == '2':
            result = subtract(num1, num2)
            operation = "вычитания"
        elif choice == '3':
            result = multiply(num1, num2)
            operation = "умножения"
        elif choice == '4':
            result = divide(num1, num2)
            operation = "деления"
        else:
            print("Неверный выбор операции!")
            return

        print(f"Результат {operation} чисел: {result}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
