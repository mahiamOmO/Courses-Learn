# if...elif...else
age = int(input("Please enter the age of the person: "))
if age < 5:
    print("Too young")
elif age == 5:
    print("Kindergarten")
elif 5 < age <= 17:
    grade = age - 5
    print("Go to {} grade".format(grade))
else:
    print("Go to College")

# Nested if
# In this program, we input a number
# check if the number is positive,
# negative, or zero and display
# an appropriate message.
# This time we use nested if
num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
