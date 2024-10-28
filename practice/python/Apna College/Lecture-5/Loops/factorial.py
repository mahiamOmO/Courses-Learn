#while loop
n = 3
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("factorial =", fact)

#for loop

n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print("factorial =", fact)
