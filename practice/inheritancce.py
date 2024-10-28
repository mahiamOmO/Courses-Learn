class Car:
    @staticmethod
    def start():
        print("Car started...")
    @staticmethod
    def stop():
        pprint("Car stopped...")

class ToyotaCar (Car):
    def __init__(self,name):
        self.name = name

car1 = ToyotaCar("fortune")
car1 = ToyotaCar("prius")
print(car1.name)