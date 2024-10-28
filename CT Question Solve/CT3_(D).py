1.

class Event:
    def __init__(self, event_name, location):
        self.event_name = event_name
        self.location = location

    def display_event_details(self):
        print(f"Event Name: {self.event_name}")
        print(f"Location: {self.location}")

2.

class Course:
    def __init__(self, course_name):
        self.course_name = course_name

class OnlineCourse(Course):
    def __init__(self, course_name, platform):
        super().__init__(course_name)
        self.platform = platform

3.

class Recipe:
    def __init__(self, recipe_name, cooking_time):
        self.recipe_name = recipe_name
        self.cooking_time = cooking_time
    def show_recipe_info(self):
        print(f"Recipe Name: {self.recipe_name}")
        print(f"Cooking Time: {self.cooking_time} minutes")


4.



class Employee:
    def __init__(self, employee_name):
        self.employee_name = employee_name

class Manager(Employee):
    def __init__(self, employee_name, department):
        super().__init__(employee_name)
        self.department = department
    def show_manager_details(self):
        print(f"Name: {self.employee_name}, Department: {self.department}")