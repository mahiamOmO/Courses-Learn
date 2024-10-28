#Implicit Type Conversion

num_int = 123
num_flo = 1.23

num_new = num_int + num_flo
print("datatype of num_int:",type(num_int))
print("datatype of num_flo:",type(num_flo))
print("value of num_new:",(num_new))
print("datatype of num_new:",type(num_new))


#Addition of string (higher) data type and integer(lower)datatype
num_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str:",type(num_str))

#Error: Explicit conversion will not work here
#print(num_int+num_str)


#Explicit type conversion
num_int = 123
num_str = "456"

print("Data type of num_int:"type(num_int))
print("Data type of num_str before type casting:",type(num_str))

num_str = int(num_str) #converting string to int
print("Data type of num_str after type casting:",type(num_str))

num_str = num_int + num_str
print("sum of num_int and num_str:",(num_sum))
print("Data type of the sum:",type(num_sum))
