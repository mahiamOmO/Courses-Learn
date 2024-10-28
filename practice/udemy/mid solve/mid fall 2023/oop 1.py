# Main class to represent common features of all vehicles
class Vehicle:
    def __init__(self, brand, model, year_of_manufacture):
        self.brand = brand
        self.model = model
        self.year_of_manufacture = year_of_manufacture
    
    # Method to describe the vehicle
    def describe(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year of Manufacture: {self.year_of_manufacture}"
