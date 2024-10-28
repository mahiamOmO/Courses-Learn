# Main program
if __name__ == "__main__":
    # Creating an object of the Car class
    my_car = Car("Toyota", "Corolla", 2021, 15, "Petrol", 4)
    
    # Using the describe method to print details
    print(my_car.describe())
    
    # Calculating and printing the mileage
    print(my_car.calculate_mileage())
