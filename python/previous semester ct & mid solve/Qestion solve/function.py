#Question 1a:
#Task: Write a Python function that takes a number of positional arguments (int) and returns the average and the summation of those numbers. You do not have to take user input.

#Example function calls:

#fun(1, 2, 3, 4, 5) returns (3, 15) (average and sum).
#fun(1, 2) returns (1.5, 3).


def fun(*args):
    total = sum(args)  # Calculate the sum of the numbers
    average = total / len(args) if len(args) > 0 else 0  # Calculate the average
    return average, total  # Return a tuple containing the average and sum

# Example function calls:
print(fun(1, 2, 3, 4, 5))  # Output: (3, 15)
print(fun(1, 2))  # Output: (1.5, 3)



#Question 1b:
#Task: Analyze the provided Python code to determine the final output after its execution. Then, justify your conclusion.

addition = 0
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

output = my_list[-2::-2]  # slices the list
print(output)

for i in output:
    if (i // 2) == 0:
        addition += i

print(addition)
