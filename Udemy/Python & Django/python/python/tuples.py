# Accessing elements of a tuple
numbers = (1, 2, 3)
print(numbers[1])    # Output: 2
print(numbers[-1])   # Output: 3

# Slicing a tuple
names = ("perry", "smith", "john", "kiwi")
print(names[2:4])    # Output: ('john', 'kiwi')

# Modifying a tuple by converting it to a list
names = ("perry", "smith", "john", "kiwi")
l = list(names)
l[1] = "kito"
t = tuple(l)         # Convert the modified list back to a tuple
print(t)             # Output: ('perry', 'kito', 'john', 'kiwi')

# Iterating over a tuple
names = ("perry", "smith", "john", "kiwi")
for name in names:
    print(name)
