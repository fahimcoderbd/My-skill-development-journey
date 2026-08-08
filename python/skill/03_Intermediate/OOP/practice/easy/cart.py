class Car:
    def __init__(self, brand:str, model:str, fuel:float):
        self.brand = brand
        self.model = model
        self.fuel = fuel

    #car driving
    def drive(self, km:float):
        if km <= 0: return "Invalid input!" 
        required_fuel = km / 10
        if self.fuel < required_fuel: return "Fuel has finished, Stopped driving..." #after fuel has finished, stopping car
        self.fuel -= required_fuel
        return (
            f"Driving car.... \n"
            f"Current fuel: {self.fuel} l\n"
        )

    def refuel(self, liters:float):
        if liters <= 0: return "Invalid input!" 
        self.fuel += liters
        return (
            f"{liters} of liters fuel added successfully! \n"
            f"Current fuel: {self.fuel} l \n"
        )

    def display(self):
        return (
            f"Car: {self.brand} \n"
            f"Model: {self.model} \n"
            f"Fuel: {self.fuel} l \n"
        )

#testing code
lamborgini = Car(brand="lamborgini", model="aventador", fuel=10)

print(lamborgini.display())
print(lamborgini.drive(10))
print(lamborgini.drive(0))
print(lamborgini.drive(-1))
print(lamborgini.drive(10))
print(lamborgini.refuel(70))
print(lamborgini.drive(100))
print(lamborgini.drive(800))

        
        
