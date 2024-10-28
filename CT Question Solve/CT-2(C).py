1.
def fibonacci_seris(n):
  lst1 = [0, 1]
  for i in range(n-2):
    element = lst1[-1] + lst1[-2]
    lst1.append(element)
  return lst1

print(fibonacci_seris(6))

output:[0, 1, 1, 2, 3, 5]


2.
def add_book(library_inventory, title, status):
  for key in library_inventory.keys():
    if key == title:
      library_inventory[key] = status
      return library_inventory
  library_inventory[title] = status
  return library_inventory

library_inventory = {
"The Great Gatsby": "available",

"To Kill a Mockingbird": "checked out"
}

add_book(library_inventory, "1984", "available")

add_book(library_inventory, "The Great Gatsby", "checked out")

output: {'The Great Gatsby': 'checked out',
 'To Kill a Mockingbird': 'checked out',
 '1984': 'available'}


3. 
def lucas_series(n):
  l_series = [2,1]
  for i in range(n-2):
    ele = l_series[-1] + l_series[-2]
    l_series.append(ele)
  return l_series

print(lucas_series(6))

output: [2, 1, 3, 4, 7, 11]


4.

def update_price(d, product, price):
  for key in d.keys():
    if key == product:
      d[key] = price
      return d
  d[product] = price
  return d

product_catalog = {

"Laptop": "$999",

"Smartphone": "$699"
}

update_price(product_catalog, "Tablet", "$499")

update_price(product_catalog, "Laptop", "$949")


output: {'Laptop': '$949', 'Smartphone': '$699', 'Tablet': '$499'}


5.

def tribonacci_series(n):
  tri_list = [0,1,1]
  for i in range(n-3):
    ele = tri_list[-1] + tri_list[-2] + tri_list[-3]
    tri_list.append(ele)
  return tri_list

# Example usage
n = 7
print(tribonacci_series(n))


output: [0, 1, 1, 2, 4, 7, 13]


6.

def add_contact(contact_book, name, phone_number):
  for key in contact_book.keys():
    if key == name:
      contact_book[key] = phone_number
      return contact_book
  contact_book[name] = phone_number
  return contact_book

contact_book = {
    "Alice": "123",
    "Bob": "987"
}
print(add_contact(contact_book, "Charlie", "555"))
print(add_contact(contact_book, "Alice", "111"))

output: {'Alice': '123', 'Bob': '987', 'Charlie': '555'}
{'Alice': '111', 'Bob': '987', 'Charlie': '555'}