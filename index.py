#Assignment One
# Base class
class Superhero:
    def __init__(self, name, power, health):
        self.name = name
        self.power = power
        self.health = health

    def introduce(self):
        return f"I am {self.name}, my power is {self.power}!"

    def take_damage(self, amount):
        self.health -= amount
        return f"{self.name} took {amount} damage. Remaining health: {self.health}"

    def use_power(self):
        return f"{self.name} uses {self.power}!"

# Derived class 1
class FlyingHero(Superhero):
    def __init__(self, name, power, health, flight_speed):
        super().__init__(name, power, health)
        self.flight_speed = flight_speed

    def use_power(self):
        return f"{self.name} soars at {self.flight_speed} km/h and uses {self.power}!"

# Derived class 2
class StrengthHero(Superhero):
    def __init__(self, name, power, health, strength_level):
        super().__init__(name, power, health)
        self.strength_level = strength_level

    def use_power(self):
        return f"{self.name} smashes with strength level {self.strength_level} using {self.power}!"

# Creating instances
hero1 = FlyingHero("SkyWing", "Wind Blast", 100, 500)
hero2 = StrengthHero("Titan", "Earthquake Slam", 150, 900)

# Using the class methods
print(hero1.introduce())
print(hero1.use_power())
print(hero2.introduce())
print(hero2.use_power())
print(hero2.take_damage(40))

#Activity 2
# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

# Derived classes
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚢"

class Bike(Vehicle):
    def move(self):
        return "Pedaling 🚴"

# Function demonstrating polymorphism
def travel(vehicle: Vehicle):
    print(f"The vehicle is: {vehicle.move()}")

# Creating different vehicle instances
my_car = Car()
my_plane = Plane()
my_boat = Boat()
my_bike = Bike()

# Polymorphic behavior
travel(my_car)
travel(my_plane)
travel(my_boat)
travel(my_bike)
