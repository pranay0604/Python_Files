class Employee:

    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        return f"Role: {self.role}\nDepartment: {self.dept}\nSalary: {self.salary}"
    
class Engineer(Employee):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "R&D", 80000)


# emp1 = Employee("Developer", "IT", 60000)
# print(emp1.showDetails())

engg1 = Engineer("Alice", 30)
print(engg1.showDetails())

print(f"Name: {engg1.name}\nAge: {engg1.age}")

