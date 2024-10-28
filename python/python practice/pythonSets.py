# Creating sets
# Set of integers
my_set1 = {11, 33, 66, 55, 44, 22}
print(my_set1)

# Set of mixed datatypes
my_set2 = {101, "Annibha", (21, 2, 1994)}
print(my_set2)

# Duplicate values are not allowed
my_set3 = {11, 22, 33, 33, 44, 22}
print(my_set3)

# Set cannot have mutable items
# my_set4 = {1, 2, [3, 4]}  # This line is commented out because lists are mutable and cannot be in a set

# We can make set from a list
my_set5 = set([1, 2, 3, 2])
print(my_set5)
print(type(my_set5))

# We can make a list from a set
my_list1 = list({11, 22, 33, 44})
print(my_list1)

# Operations on sets
my_set1 = {11, 22, 33, 44, 66, 55}
print(my_set1)

# my_set1[0]  # Sets are unordered, so indexing is not supported

# Add one element
my_set1.add(77)
print(my_set1)

# Add multiple elements
my_set1.update([88, 99, 22])
print(my_set1)

# Add list and set
my_set1.update([100, 102], {103, 104, 105})
print(my_set1)

