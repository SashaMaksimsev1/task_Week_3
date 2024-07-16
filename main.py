def add(x, y):
    """Додавання"""
    return x + y

def subtract(x, y):
    """Віднімання"""
    return x - y

def multiply(x, y):
    """Множення"""
    return x * y

def divide(x, y):
    """Ділення"""
    if y == 0:
        return "Помилка! Ділення на нуль."
    return x / y

def calculator():
    print("Вітаємо в простому калькуляторі!")
    print("Виберіть операцію:")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")

    while True:
        choice = input("Введіть номер операції (1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Введіть перше число: "))
                num2 = float(input("Введіть друге число: "))
            except ValueError:
                print("Невірний ввід. Будь ласка, введіть числові значення.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                result = divide(num1, num2)
                if result == "Помилка! Ділення на нуль.":
                    print(result)
                else:
                    print(f"{num1} / {num2} = {result}")

            next_calculation = input("Бажаєте виконати ще одну операцію? (так/ні): ")
            if next_calculation.lower() != 'так':
                break
        else:
            print("Невірний вибір. Будь ласка, виберіть операцію (1/2/3/4).")

if __name__ == "__main__":
    calculator()
