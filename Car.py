# Inheritance in Python
# Single and Multilevel Inheritance 

class Car:

    # color = "Black"  # Inherited Attribute

    def __init__(self, type):
        self.type = type

    @staticmethod
    def start_engine():
        return "Engine Started..."
    
    @staticmethod
    def stop_engine():
        return "Engine Stopped..."
    
class Toyota_Car(Car):

    def __init__(self, name, type):
        super().__init__(type)
        self.name = name

class Fortuner(Toyota_Car):
    
    def __init__(self, type):
        self.type = type

# car1 = Fortuner("Petrol")
# print(car1.start_engine())
# print(car1.stop_engine())

# T1 = Toyota_Car("Fortuner")
# T2 = Toyota_Car("Innova")
# print(T1.color)  # Inherited Attribute
# print(T1.start_engine())  # Inherited Method
# print(T1.stop_engine())  # Inherited Method

car1 = Toyota_Car("Innova", "Diesel")
print(car1.name)
print(car1.type)

# Multiple Inheritance

class A:

    varA = "Welcome to class A"

class B:

    varB = "Welcome to class B"

class C(A, B):

    varC = "Welcome to class C"

c1 = C()
print(c1.varA)  # Inherited from class A
print(c1.varB)  # Inherited from class B
print(c1.varC)  # Own Attribute



