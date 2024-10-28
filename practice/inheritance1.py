class Car:
    @staticmethod
    def start():
        print("Car started...")
    @staticmethod
    def stop():
        pprint("Car stopped...")

class Toyota(Car):
    def __init__(self,brand):
        self.brand = brand

class Fortune(Toyota):
    def __init__(self,type):
        self.type = type

car1 = Fortune("diesel")
car1.start()