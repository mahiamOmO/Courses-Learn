1.
def simple_calculator(num1, num2, op):
  if op == "add":
    return num1 + num2
  elif op == "sub":
    return num1 - num2
  elif op == "mul":
    return num1 * num2
  elif op == "div":
    return num1/num2
  else:
    return "Error"


print(simple_calculator(10,5,"mul"))
output: 50

2.

def count_item_frequency(list1):
  d = {}
  for i in list1:
    if i in d:
      d[i]+=1
    else:
      d[i]=1
  return d

items = ["apple", "banana", "apple", "orange", "banana", "banana"]

print(count_item_frequency(items))

{'apple': 2, 'banana': 3, 'orange': 1}

3.
def classify_grade(grade):
  if grade >= 90:
    return 'A'
  elif grade >= 80:
    return 'B'
  elif grade >= 70:
    return 'C'
  elif grade >= 60:
    return 'D'

print(classify_grade(85))

output: B

4.
def find_total_marks(students, name):
  '''for key in students.keys():
    if key == name:
      return students[key]
  return "Student does not exist"'''

  if name in students:
    return students[name]
  return "Student does not exist"

students_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 88
}

print(find_total_marks(students_marks, "Bob"))
output: 92


5.

def string_formatter(str1,str2, op):
  if op == "combine":
    return str1 + str2
  if op == "uppercase":
    return str1.upper() + str2.upper()
  if op == "lowercase":
    return str1.lower() + str2.lower()
  if op == "reverse":
    return str1 + str2[::-1]
  return

print(string_formatter("Hello", "World", "reverse"))


output :HellodlroW

6.

def delete_contact(contact_book, name, phone_number):
  for key in contact_book.keys():
    if key == name and contact_book[key] == phone_number:
      del contact_book[key]
      return contact_book
  return "The phone number does not exist"


contact_book = {
    "Alice": "123",
    "Bob": "987"
}

print(delete_contact(contact_book, "Alice", "123"))

output: {'Bob': '987'}