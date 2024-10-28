# Iterating through a string 
letter_count = 0
for letter in 'Hello World':
    letter_count += 1
    print(letter_count, 'times 1 letter has been found')

# String membership
print('1' in "hello")
print('1' not in "hello")
print('b' in "hello")
print('b' not in "hello")

# Built-in function

mystr = 'university'

# Using enumerate()
my_list_enumerate = list(enumerate(mystr))
print('list(enumerate(mystr)):', my_list_enumerate)

# Using character count 
print('len(mystr) =', len(mystr))

# String character count 
print('len(mystr) =', len(mystr))

# String formatting using escape sequence
#print('tell me "what\'s your name?"')

# Using triple quotes
print('''tell me "what's your name?"''')

# Escaping single quotes
#print('tell me "what's your name?"')

# Escaping single quotes
print("tell me 'what\'s your name?'")

# Escaping double quotes 
print("tell me \"what's your name?\"")

# format() method
# Default (implicit) order
default_order = "{} {} and {}".format('Today', 'is', 'Sunday')
print(default_order)

# Order using positional argument
positional_order = "{1} {0} and {2}".format('is', 'Today', 'Sunday')
print(positional_order)

# Order using keyword argument
keyword_order = "{t} {i} and {s}".format(i='is', t='Today', s='Sunday')
print(keyword_order)

# Formatting numbers
print("Required binary representation of {0} is {0:b}".format(20))

# Formatting floats
print("Exponent representation: {0:e}".format(1566.345))

# Round off
print("One third is: {0:.3f}".format(1/3))

# String methods
print("gOOD moRNing tO all".lower())
print("gOOD moRNing tO all".upper())
print("gOOD moRNing tO all".find('tO'))
print("gOOD moRNing tO all".replace('all', 'everybody'))
