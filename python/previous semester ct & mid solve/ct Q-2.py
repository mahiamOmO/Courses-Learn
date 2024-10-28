#Q2:

#Task: Write a Python function that takes a list of numbers and returns the absolute difference between the sum of numbers at odd indices and the sum of numbers at even indices.
#Given numbers = [5, 10, 15, 20, 25, 30]
#Expected Output:
#15


def absolute_difference(numbers):
    # Calculate sum of numbers at even indices
    even_sum = sum(numbers[i] for i in range(0, len(numbers), 2))
    
    # Calculate sum of numbers at odd indices
    odd_sum = sum(numbers[i] for i in range(1, len(numbers), 2))
    
    # Return the absolute difference
    return abs(even_sum - odd_sum)

# Example list
numbers = [5, 10, 15, 20, 25, 30]

# Calling the function
print(absolute_difference(numbers))
