def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2

while True:
    print("Operation Menu -\n"
          "1. Addition of two numbers\n"
          "2. Subtraction of two numbers\n"
          "3. Multiplication of two numbers\n"
          "4. Division of two numbers\n"
          "5. Exit\n")
    select = input("Select operations from 1, 2, 3, 4, 5: ")

    if select in ('1', '2', '3', '4'):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if select == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif select == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif select == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif select == '4':
            if num2 != 0:
                print(num1, "/", num2, "=", divide(num1, num2))
            else:
                print("Division by zero is not allowed!")
    elif select == '5':
        print("Exiting...")
        break
    else:
        print("Invalid input!")
