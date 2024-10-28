# my_list = [5, 10, 15, 20, 25, 30, 35, 40, 45]
# Write a list slicing command to obtain the output [10, 25, 40] from my_list.
# Write a list slicing command to obtain the output [45, 40, 35] from my_list.
# What is the output of the code : print(my_list.pop() == my_list[-1])
# Write code to add all the elements of my_list. Print the sum.
# With the string my_string = "Hello, World!", how can you slice the s

my_list = [5, 10, 15, 20, 25, 30, 35, 40, 45]

# Output: [10, 25, 40]
print(my_list[1:8:3])

# Output: [45, 40, 35]
print(my_list[-1:-4:-1])


print(my_list.pop() == my_list[-1])


# Add all the elements of my_list
sum_of_elements = sum(my_list)
print(sum_of_elements)


my_string = "Hello, World!"
print(my_string[7:12])


my_list = [5, 10, 15, 20, 25, 30, 35, 40, 45]
print(my_list[-1:-4])


# prompt: Take an integer as input from the user and check whether he/she is eligible to vote or not. If not, then check how many years it will be until he/she can vote.

age = int(input("Enter your age: "))

if age >= 18:
  print("You are eligible to vote.")
else:
  years_left = 18 - age
  print("You are not eligible to vote.")
  print("You will be eligible to vote in", years_left, "years.")

# prompt: You are given a list of integers. Write a Python code snippet to count the even and odd numbers in the list. Print the total counts for each, and then print "More evens" if there are more even numbers, or "More odds" if there are more or an equal number of odd numbers.
# Suppose the list is : numbers = [12, 7, 5, 8, 14, 9, 22, 13, 18, 21]. You do not have to take user input.

numbers = [12, 7, 5, 8, 14, 9, 22, 13, 18, 21]
even_count = 0
odd_count = 0

for number in numbers:
  if number % 2 == 0:
    even_count += 1
  else:
    odd_count += 1

print("Total even numbers:", even_count)
print("Total odd numbers:", odd_count)

if even_count > odd_count:
  print("More evens")
else:
  print("More odds")