class valueLessThanZeroError(Exception):
    pass

class aLessThanBError(Exception):
    pass

def add(a, b):
    c = a + b
    return c

def sub(a, b):
    if a < b:
        raise aLessThanBError
    c = a - b
    return c

def multi(a, b):
    c = a * b
    return c

def divi(a, b):
    if b == 0:
        raise ZeroDivisionError
    c = a / b
    return c

ch = 1
while ch != 0:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Quit Calculator")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a valid option.")
        continue

    if choice == 5:
        ch = 0
    elif choice in [1, 2, 3, 4]:
        try:
            x = float(input("Enter the Value of A: "))
            y = float(input("Enter the Value of B: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        result = 0

        try:
            if choice == 1:
                result = add(x, y)
                print("The result is:", result)
            elif choice == 2:
                try:
                    result = sub(x, y)
                    print("The result is:", result)
                except aLessThanBError:
                    print("A is less than B for subtraction.")
            elif choice == 3:
                result = multi(x, y)
                print("The result is:", result)
            elif choice == 4:
                try:
                    result = divi(x, y)
                    print("The result is:", result)
                except ZeroDivisionError:
                    print("Division by zero is not allowed!")
        except aLessThanBError:
            print("A is less than B for a choice other than subtraction.")
    else:
        print("Invalid choice. Please enter a valid option (1-5).")
