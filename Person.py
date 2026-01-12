# class Person:
 
#     __name = "Anonymous" # Private Attribute


#     def __hello(self):  # Private Method
#         print("Hello Person !!!")

#     def welcome(self):
#         self.__hello()

# P1 = Person()

# P1.welcome()

class Person:

    name = "Anonymous" 

    # def changeName(self, name):
        # self.__class__.name = name
        # Person.name = name

    @classmethod
    def changeName(cls, name):
        cls.name = name

P1 = Person()
P1.changeName("Pranay")
print(P1.name)
print(Person.name)

