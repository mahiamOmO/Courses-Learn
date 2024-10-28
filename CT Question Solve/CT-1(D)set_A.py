# prompt: Guess the output:
# x= 113 % 5
# if x % 2 == 0:
#     if x % 3 == 0:
#         output = "Divisible by both 2 and 3"
#     else:
#         output = "Divisible by 2 only"
# else:
#     output = "Not divisible by 2"
# print(output)

x =178% 9
if x % 2 == 0:
    if x % 3 == 0:
        output = "Divisible by both 2 and 3"
    else:
        output = "Divisible by 2 only"
else:
    output = "Not divisible by 2"
print(output)

Not divisible by 2


# prompt: Guess the output:
# x= 113 % 5
# if x % 2 == 0:
#     if x % 3 == 0:
#         output = "Divisible by both 2 and 3"
#     else:
#         output = "Divisible by 2 only"
# else:
#     output = "Not divisible by 2"
# print(output)

x= 151 % 5
if x % 2 == 0:
    if x % 3 == 0:
        output = "Divisible by both 2 and 3"
    else:
        output = "Divisible by 2 only"
else:
    output = "Not divisible by 2"
print(output)

Not divisible by 2


# prompt: my_list = [3, 6, 9, 15, 15]
# output = my_list.pop() + my_list[-1]
# print(output)

my_list = [3, 6, 9, 15, 15]
output = my_list.pop() + my_list[-1]
print(output)

30

# prompt: my_list = [3, 6, 9, 12, 15]
# output = my_list.pop() + my_list[-1]
# print(output)

my_list = [3, 6, 9, 12, 15]
output = my_list.pop() + my_list[-1]
print(output)

27


 prompt: Takebirth year as an integer input from the user and calculate their current age. Check whether they are eligible for a senior citizen discount (age 60 or older). If not, calculate how many more years they have until they qualify for the discount.

birth_year = int(input("Enter your birth year: "))
current_year = int(input("Enter current year: "))
age = current_year - birth_year

if age >= 60:
  print("You are eligible for a senior citizen discount!")
else:
  years_to_discount = 60 - age
  print("You are not yet eligible for a senior citizen discount.")
  print(f"You will be eligible in {years_to_discount} years.")

Enter your birth year: 1950
Enter current year: 2024
You are eligible for a senior citizen discount!
   

# prompt: You are given a list of words. Write a Python code snippet to find and print the longest word in the list. If there is a tie (multiple words with the same maximum length), print all such words. If the list is empty, print "The list is empty."
# Suppose the list is: words = ["apple", "banana", "grapefruit", "kiwi", "orange"]. You do not have to take user input.

words = ["apple", "banana", "grape", "kiwi", "orange"]

if not words:
  print("The list is empty.")
else:
  max_length = 0
  longest_words = []
  for word in words:
    if len(word) > max_length:
      max_length = len(word)
      longest_words = [word]
      print(longest_words)
    elif len(word) == max_length:
      longest_words.append(word)

  print("Longest word(s):", longest_words)

['apple']
['banana']
Longest word(s): ['banana', 'orange']


words = ["apple", "banana", "grape", "kiwi", "orange"]
if not words:
  print('list is empty')
else:
  cleaned_words = [word.strip() for word in words]
  max_length = max(len(word) for word in cleaned_words)
  longest_words = [word for word in cleaned_words if len(word) == max_length]
  print('Longest word(s):', longest_words)

Longest word(s): ['banana', 'orange']


words = ["apple", "banana", "grape", "kiwi", "orange"]

#for i in range(0,len(words)):
for j in range(0, len(words)-1):
    if len(words[j]) >= len(words[j+1]):
      temp = words[j]
      words[j] = words[j+1]
      words[j+1] = temp
max_len = len(temp)
if max_len != 0:
  for j in words:
    if len(j) == max_len:
      print(j)
else:
  print('list is empty')

orange
banana
