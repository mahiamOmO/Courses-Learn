# prompt: my_list = [1,3,5,7,9,11,13,15,17]
# Write a list slicing command to obtain the output [3,9,15] from my_list.
# Write a list slicing command to obtain the output [17,15,13] from my_list.
# What is the output of the code : print (my_list[-1] == (my_list.pop())
# Write code to add all the elements of my_list. Print the sum.
# With the string my_string = "Hello, World!", how can you slice the string to obtain "Hello"

my_list = [1,3,5,7,9,11,13,15,17]

# Output: [3, 9, 15]
print(my_list[1:8:3])

# Output: [17, 15, 13]
print(my_list[-1:-4:-1])


print(my_list[-1] == my_list.pop())


# Add all the elements of my_list
sum_of_elements = sum(my_list)
print(sum_of_elements)


my_string = "Hello, World!"
print(my_string[:5])


[3, 9, 15]
[17, 15, 13]
True
64
World