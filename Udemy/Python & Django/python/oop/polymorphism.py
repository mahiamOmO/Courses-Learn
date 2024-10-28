class Bulbil:
    def fly(self):
        print("bulbil can fly")

    def swim(self):
        print("bulbil can't swim")

class Ostriches:
    def fly(self):
        print(" Ostriches can fly")

    def swim(self):
        print("Ostriches can't swim")

def flying_test(bird):
    bird.fly()

blue = Bulbil()
blue.fly()

ostri = Ostriches()


flying_test(blue)

flying_test(ostri)