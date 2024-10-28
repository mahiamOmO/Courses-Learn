class Dog:
    species = "Canis familiaris"  # Class attribute

    def __init__(self, name, age):  # Corrected constructor syntax
        self.name = name
        self.age = age

    def bark(self):  # Corrected method name to "bark"
        print("Woof!")

# Creating an instance of Dog
my_dog = Dog(name="Buddy", age=3)

# Accessing attributes
dog_name = my_dog.name
dog_age = my_dog.age
dog_species = my_dog.species

# Calling method
my_dog.bark()

# Printing information
print(f"Name: {dog_name}")
print(f"Age: {dog_age}")
print(f"Species: {dog_species}")
