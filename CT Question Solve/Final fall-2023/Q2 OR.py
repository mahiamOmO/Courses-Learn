# 2 OR 
# a solution:
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name} Age: {self.age} Salary: {self.salary}")

# b :

class FullTimeEmployee(Employee):
    def __init__(self, name, age, salary, bonus):
        super().__init__(name, age, salary)
        self.bonus = bonus

    def calculate_total_salary(self):
        return self.salary + self.bonus

# c
class PartTimeEmployee(Employee):
    def __init__(self, name, age, salary, hours_worked):
        super().__init__(name, age, salary)
        self.hours_worked = hours_worked

    def calculate_payment(self, hourly_rate):
        return self.hours_worked * hourly_rate

