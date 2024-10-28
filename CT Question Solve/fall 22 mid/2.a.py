# Taking inputs for X and Y
X = int(input("Enter the value of X: "))
Y = int(input("Enter the value of Y: "))

# Using a for loop to find numbers divisible by 5 between X and Y
for num in range(X + 1, Y):
    if num % 5 == 0:
        print(num)
