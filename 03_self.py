class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    # Static method, means the function does'nt requires the need of object
    @staticmethod       # decorator to marks greet as a static method
    def greet():
        print("Good morning")

rishabh = Employee()
rishabh. language = "JavaScript" # This is an instance attribute
rishabh.greet()
rishabh.getInfo()
# Employee.getInfo(rishabh)