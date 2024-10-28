1.
class Person:
    def __init__(self, nid, email):
        self.nid = nid
        self.email = email

    def display_full_name(self):
        # Replace with actual logic to retrieve full name based on nid or other data
        print("Full Name: [Logic to get full name]")


2.

class Course:
    def __init__(self, course_name):
        self.course_name = course_name

class OnlineCourse(Course):
    def __init__(self, course_name, platform):
        super().__init__(course_name)
        self.platform = platform

    def display_course_info(self):
        print(f"Course: {self.course_name}, Platform: {self.platform}")


online_course = OnlineCourse("Python Programming", "CSE309")
online_course.display_course_info()

outut: Course: Python Programming, Platform: CSE309


3.

class Student:
    def __init__(self, student_id, major):
        self.student_id = student_id
        self.major = major

    def display_student_info(self):
        print(f"Student ID: {self.student_id}, Major: {self.major}")


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