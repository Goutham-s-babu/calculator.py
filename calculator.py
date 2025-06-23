
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b


while True:
    print("\n===== Calculator Menu =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '5':
        print("Thanks for using the calculator. Goodbye!")
        break

    num1_input = input("Enter the first number: ")
    num2_input = input("Enter the second number: ")

    try:
        num1 = float(num1_input)
        num2 = float(num2_input)
    except ValueError:
        print("Invalid number input. Please enter numeric values.")
        continue

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
