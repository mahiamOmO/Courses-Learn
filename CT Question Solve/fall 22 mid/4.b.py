# Function that uses *args to accept a variable number of arguments
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

# Example call with multiple arguments
result = sum_all(10, 20, 30, 40)
print(f"The sum of the numbers is: {result}")
