first = 'alice'
last = 'mary'
message = first  + '[' + last + '] is a software engineer'
print(message)
message = first   + last + 'is a software engineer'
print(message)

msz = f'{first} {last} is a software engineer'
print(msz)

msz = f'{first} [{last}] is a software engineer'
print(msz)