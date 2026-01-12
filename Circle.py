class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return round(math.pi * (self.radius ** 2),2)

    def circumference(self):
        import math
        return round(2 * math.pi * self.radius,2)
    
circle1 = Circle(7)
print("Area of Circle:", circle1.area())
print("Circumference of Circle:", circle1.circumference())

