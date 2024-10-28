class Student:
    college_name = "Abc college"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("Welcome Student", self.name)

    def get_marks(self):
        return self.marks

# Creating an instance of Student
s1 = Student("Karan", 97)
s1.welcome()

# Getting the marks
print(s1.get_marks())
