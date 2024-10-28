class Mammal:
     def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("bark")
class Cat(Mammal):
    def sleep(self):
        print(" i am sleeping")

puppy = Dog()
puppy.walk()

cat1 = Cat()
cat1.sleep()

puppy = Dog()
puppy.walk()