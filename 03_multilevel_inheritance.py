class Employee:
    a = 1
    name = "Rishabh"
    company = "ITC"
    def employee(self):
        print(f"The Employee's name is {Employee.name} from the {self.company} company")

class Programmer(Employee):
    b = 2
    name = "Krishna"
    company = "ITC"
    def programmer(self):
        print(f"The Programmer's name is {Programmer.name} from the {self.company} company")

class Manager(Programmer):
    c = 3
    name = "Vansh"
    company = "ITC"
    def manager(self):
        print(f"The Manager of {Programmer.name} (Programmer) is {Manager.name} from the {self.company} company")

# o = Employee()
# print(o.a) # Prints the a attribute
# # print(o.b) # Shows an error as there is no b attribute in Employee class

# o = Programmer()
# print(o.a, o.b)

# o = Manager()
# print(o.a, o.b, o.c)

e = Employee()
p = Programmer()
m = Manager()

m.employee()
m.programmer()
m.manager()

'''
MULTILEVEL INHERITANCE:
When a child class becomes a parent for another child class.
'''