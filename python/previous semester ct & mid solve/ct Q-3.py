#Q1: Write a Python program to remove empty strings from a list of strings.
#Sample Input:
#list1 = ["A", "", "E", "K", "", "B"]
#Expected Output:
#["A", "E", "K", "B"]



#Solution:

# List with empty strings
list1 = ["A", "", "E", "K", "", "B"]

# Use list comprehension to filter out empty strings
filtered_list = [string for string in list1 if string]

# Output the filtered list
print(filtered_list)





#Q2: Write a Python program to check if two sets have any elements in common. If yes, display the common elements.
#Sample Input:
#set1 = {10, 20, 30, 40, 50}
#set2 = {60, 70, 80, 90, 10}

#Expected Output:
#{10}


# Two sets
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

# Find common elements using intersection
common_elements = set1.intersection(set2)

# Output the result
if common_elements:
    print(f"Two sets have items in common: {common_elements}")
else:
    print("No common elements found")





#Problem: You have a dictionary stocks with stock symbols as keys and prices as values. The task is to increase the prices by 10% and add them to a new dictionary (new_stocks) only if the prices are greater than 300.

# Given dictionary of stocks and prices
stocks = {
    "P-1": 421,
    "P-2": 108,
    "P-3": 319
}

# New dictionary to store updated stocks with prices greater than 300
new_stocks = {}

# Loop through the stocks and update the prices
for stock, price in stocks.items():
    if price > 300:
        new_stocks[stock] = price * 1.10  # Increase price by 10%

# Output the new dictionary
print(new_stocks)
