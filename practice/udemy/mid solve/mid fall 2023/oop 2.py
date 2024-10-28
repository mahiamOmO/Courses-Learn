# Subclass Car that inherits from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, year_of_manufacture, mileage, fuel_type, number_of_doors):
        super().__init__(brand, model, year_of_manufacture)
        self.mileage = mileage
        self.fuel_type = fuel_type
        self.number_of_doors = number_of_doors
    
    # Method to calculate and return mileage
    def calculate_mileage(self):
        return f"Mileage: {self.mileage} km/l"
    
    # Overriding the describe method to include additional car details
    def describe(self):
        base_description = super().describe()
        return f"{base_description}, Mileage: {self.mileage}, Fuel Type: {self.fuel_type}, Number of Doors: {self.number_of_doors}"
