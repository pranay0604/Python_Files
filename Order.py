# Operator Overloading using Greater Than (>) Operator
# Using Dunder Method __gt__()

class Order:

    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price


odr1 = Order("Chips", 50)
odr2 = Order("Coffee", 30)

print(odr1 > odr2) # True



