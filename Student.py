class Student:

    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str(round((self.phy + self.chem + self.math) / 3, 2)) + "%"

    # def calcPercentage(self):
    #     self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

    

stud1 = Student(80, 80, 70)
print(stud1.percentage)

stud1.phy = 95
# print(stud1.phy)
# stud1.calcPercentage()
print(stud1.percentage)

