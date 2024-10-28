class Employee:
    def __init__(self):
        self.name = "admin"
        self.salary = 2000

    def show(self):
        print(self.name)
        print(self.salary)

e1 = Employee() 


print('This is a Dictionary:', vars(e1))
