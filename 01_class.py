class Employee:
    language = "Py"     # This is a class attribute.
    salary = 1200000

rishabh = Employee()
rishabh.name = "Rishabh"    # This is a instance attribute.
print(rishabh.name, rishabh.language, rishabh.salary)

krishna = Employee()
krishna.name = "Krishna Robinson"
print(krishna.name, krishna.salary, krishna.language)

# Here name is object attribute and salary and language are class attributes as they directly belong to the class.

'''
The concept focuses on using reusable code (DRY Principle).

CLASS
A class is a blueprint for creating object.

OBJECT
An object is an instantiation of a class. When class is defined, a template (info) is defined. 
Memory is allocated only after object instantiation.

Objects of a given class can invoke the methods available to it without revealing the
implementation detailed to the user. - Abstractions & Encapsulation!

MODELLING A PROBLEM IN OOPS
We identify the following in our problem.

. Noun - Class - Employee
· Adjective -  Attributes - name, age, salary
· Verbs - Methods - getSalary(), increment()

CLASS ATTRIBUTES
An attribute that belongs to the class rather than a particular object.

'''
