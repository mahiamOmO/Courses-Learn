# Program to print only the even numbers between 1 and 19 using continue
for i in range(1, 20):
    if i % 2 != 0:
        continue  # Current iteration gets skipped
    print(i)

