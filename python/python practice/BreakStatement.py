import random as r

# Generate a random number between 1 and 19
rand_num = r.randrange(1, 20)
print("Number to be guessed:", rand_num)

i = 1
while True:
    print("Number Guessed:", i)
    if i == rand_num:  # If the number guessed is the random number, this block will be executed
        print("Random Number has been guessed Successfully!")
        break  # Break statement stops and exits from the loop
    i += 1


