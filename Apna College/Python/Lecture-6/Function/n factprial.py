# 1 solution
n = 5
fact = 1  # Initialize fact to 1
for i in range(1, n+1):
    fact *= i
print(fact)

# 2 solution

def cal_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)
cal_fact(6)