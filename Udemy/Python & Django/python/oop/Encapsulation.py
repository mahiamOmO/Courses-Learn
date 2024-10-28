class Lappy():
    def __init__(self):
        self. __maxprice = 25000

    def sell(self):
        print("Selling orice of lappy: {}.format(self. __maxprice)")

    def setMaxprice(self,price):
        self. __maxprice = price

c = Lappy()
c.sell()

c. __maxprice = 3000
c.sell()


c.setMaxprice(3000)
c.sell()