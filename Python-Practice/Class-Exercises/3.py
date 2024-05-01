class Car:
    def __init__ (self, plate, brand, year):
        self.plate = plate
        self.brand = brand
        self.year = year

Whip = Car("D37L55", "Lambo", "2025")

print(Car.__dict__)
