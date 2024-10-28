# Recursive function to find the GCD of two numbers
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Taking input for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calling the gcd function and displaying the result
result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result}")
