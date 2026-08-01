class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show_info(self):
        print(f"Vehicle brand: {self.brand}")
        print(f"Vehicle speed: {self.speed} km/h")


class Car(Vehicle):
    def __init__(self, brand, speed, doors):
        super().__init__(brand, speed)
        self.doors = doors

    def show_info(self):
        super().show_info()
        print(f"Doors: {self.doors}")


class Bike(Vehicle):
    def __init__(self, brand, speed, bike_type):
        super().__init__(brand, speed)
        self.bike_type = bike_type

    def show_info(self):
        super().show_info()
        print(f"Type: {self.bike_type}")


# objects
car1 = Car("Lamborghini", 120, 2)
bike1 = Bike("Kawasaki", 300, "Sports")

car1.show_info()
print("------")
bike1.show_info()