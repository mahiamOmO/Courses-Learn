numbers = [5,10,15,20,25]
sum = 0
for num in numbers:
    print(num)
    sum = sum + num
    if sum > 20:
        print('bigger values')
print(sum)


#another example
text = 'pagla hawa'
for char in text:
    print(char)

#range
print(range(1,10))

#range another example
for i  in range(1,10,2):
    print(i)

#another rnage example

friends = ['nobel', 'ashir', 'tasfir', 'naz']

for friend in friends:
    print(friend)
