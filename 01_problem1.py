# Create a Class "Programmer" for storing information of few programmers working at Microsoft

class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Rishabh", 1200000, 483113)
print(p.name, p.salary, p.pin, p.company)

k = Programmer("Krishna", 1400000, 783411)
print(k.name, k.salary, k.pin, k.company)