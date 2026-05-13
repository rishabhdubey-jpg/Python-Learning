class Employee:
    language = "Python"     # This is a class attribute.
    salary = 1200000

rishabh = Employee()
rishabh.language = "Javascript"    # This is a instance attribute.
print(rishabh.language, rishabh.salary)