arr = [10, 20, 30, 40, 50]
print(arr)

print(arr[0])
print(arr[1])
print(arr[2])
print(arr[-1])
print(arr[-2])

brands = ['Coke', 'Apple', 'Google', 'Microsoft', 'Toyota']
print(brands)

num_brands = len(brands)
print(num_brands)

brands.append("Intel")
print(brands)

colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
del colors[4]
colors.remove("blue")
colors.pop(3)
print(colors)

fruits = ["Apple", "Banana", "Mango", "Grapes"]
fruits[1] = "pineapple"
fruits[2] = "Guava"
print(fruits)

concat = [1, 2, 3]
concat = [4, 5, 6]
print(concat)

repeat = ["a"]
repeat = repeat * 5
print(repeat)
