# creating an empty tuple
tuple1 = ()
print(tuple1)

# creating tuple with integer elements
tuple2 = (1, 2, 3)
print(tuple2)

# with mixed datatypes
tuple3 = (101, "Aniban", 200.00, "HR dept")
print(tuple3)

# creating of nested tuple
tuple4 = ("Points", [1, 2, 3], (7, 8, 6))
print(tuple4)

# tuple can be created without any parentheses
# also called tuple packing

tuple5 = 101, "Aniban", 2000.00, "HR Dept"

# tuple unpacking is also possible
empid, empname, empsal, empdept = tuple5

print(empid)
print(empname)
print(empsal)
print(empdept)
print(type(tuple5))

# accessing elements in a tuple
tuple1 = ('w', 'e', 'l', 'c', 'o', 'm', 'e')

print(tuple1)
print(tuple1[1])
print(tuple1[3])
print(tuple1[5])

# nested tuple
nest_tuple = ("points", [1, 3, 4], (8, 7, 9))
print(nest_tuple)
print(nest_tuple[0][3])
print(nest_tuple[1][2])
print(nest_tuple[2][2])

# slicing tuple contents
tuple1 = ('w', 'e', 'l', 'o', 'm', 'e')
print(tuple1[1:3])
print(tuple1[:-3])
print(tuple1[3:])
print(tuple1[:])

# tuple elements are immutable
tuple1 = ('w', 'e', 'l', 'e', 'o', 'm', 'e')
print(tuple1)

# concatenation of tuples
tuple2 = ('w', 'e', 'l')
tuple3 = ('c', 'o', 'm', 'e')
print(tuple2)
print(tuple3)
print(tuple2 + tuple3)
print("again, " * 4)

# tuples cannot be modified but can be reassigned
tuple1 = ('g', 'o', 'o', 'd', 'b', 'y', 'e')
print(tuple1)

# deletion operation on a tuple
tuple4 = ('w', 'e', 'l', 'e', 'o', 'm', 'e')
# individual elements cannot be deleted but the entire tuple can be
del tuple4
# print(tuple4)  # This would cause an error since tuple4 is deleted

# tuple methods
tuple5 = ('w', 'e', 'l', 'e', 'o', 'm', 'e')
print(tuple5.count('e'))
print(tuple5.index('e'))

# tuple operations
tuple6 = ('w', 'e', 'l', 'e', 'o', 'm', 'e')

# membership
print('c' in tuple6)
print('c' not in tuple6)
print('a' in tuple6)
print('a' not in tuple6)

# iteration through tuple elements
tuple6 = ('w', 'e', 'l', 'e', 'o', 'm', 'e')

for letter in tuple6:
    print("letter is ->", letter)

# built-in functions with tuple
tuple7 = (5, 2, 8, 1, 9, 3)
print(tuple7)
print(max(tuple7))
print(min(tuple7))
print(sorted(tuple7))
print(len(tuple7))
