# Add a static method in problem 2, to greet the user with hello.

class calculator: 
    def __init__(self, n):
        self.n = n
    
    def square(self):
        print(f"The square of {self.n} is {self.n*self.n}")
    
    def cube(self):
        print(f"The cube of {self.n} is {self.n*self.n*self.n}")
    
    def sq_root(self):
        print(f"The square root of {self.n} is {self.n**(1/2)}")

    @staticmethod
    def greet():
        print("Good morning..")

p = calculator(4)
p.greet()
p.square()
p.greet()
p.cube()
p.greet()
p.sq_root()