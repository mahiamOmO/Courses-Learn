class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Shradha")
print(s1.name)  # This will print "Shradha"

del s1.name  # This deletes the name attribute

