class example:
    def add(self, a, b, c=0):
        x = a + b + c
        return x

obj = example()

print(obj.add(10, 20, 30))  # This will output 60
print(obj.add(10, 20))      # This will output 30 (since c is 0 by default)
