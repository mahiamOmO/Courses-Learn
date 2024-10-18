class Student:
    def __init__(self, full_name="Default Name"):
        self.name = full_name
        print("Adding new Student in Database...")

# Creating instances of Student
s1 = Student("Karan")  # Pass name during initialization
print(s1.name)

s2 = Student()  # No name passed, so it will use the default name
print(s2.name)
