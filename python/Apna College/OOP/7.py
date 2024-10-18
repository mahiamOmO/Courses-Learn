class Person:  # Corrected class name
    __name = "anonymous"

    def __hello(self):  # Added self to make it an instance method
        print("Hello person!")

    def welcome(self):
        self.__hello()  # Correctly calling the __hello method

p1 = Person()  # Corrected assignment
p1.welcome()  # Call the welcome method
