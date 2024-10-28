def hello1():  # Function without a return statement
    print("Hello! I love to code in functions")

def hello2():  # Function with a return statement
    return "Hello! I love to code in Python."

# Calling the functions
hello1()
print(hello2())

def myAddition(x, y):
    print("Performing the addition operation...")
    return x + y

def mySubtraction(x, y):
    print("Performing the subtraction operation...")
    return x - y

def myMultiplication(x, y):
    print("Performing the multiplication operation...")
    return x * y

def myDivision(x, y):
    print("Performing the division operation...")
    return x / y

def myMenu():
    print("1 > Addition operation....")
    print("2 > Subtraction operation....")
    print("3 > Multiplication operation....")
    print("4 > Division operation....")
    ch = int(input("Please enter your option number: "))
    return ch

def calculation():
    ch = myMenu()

    num1 = int(input("Please enter your first number... "))
    num2 = int(input("Please enter your second number... "))

    if ch == 1:
        result = myAddition(num1, num2)
    elif ch == 2:
        result = mySubtraction(num1, num2)
    elif ch == 3:
        result = myMultiplication(num1, num2)
    elif ch == 4:
        result = myDivision(num1, num2)
    else:
        print("Invalid option selected.")
        return

    print("So, the result = ", result)

# Call the calculation function to start the program
calculation()
