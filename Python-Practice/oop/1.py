import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def find_area(self):
        return math.pi * (self.radius**2)
    
    def find_perimeter(self):
        # Aka Circumeference but "perimeter" is specified :)

        return 2 * math.pi * self.radius

# rad = float(input("Input the radius:"))
# DYNAMIC MODE

rad = 5

circle1 = Circle(rad)

print("The area is: {:.4f} and the circumference is {:.4f}".format(circle1.find_area(), circle1.find_perimeter()))
