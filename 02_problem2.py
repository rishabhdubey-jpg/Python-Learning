# Write a class "calculator" capable of finding square, cube and square root of a number.

class calculator: 
    def __init__(self, n):
        self.n = n
    
    def square(self):
        print(f"The square of {self.n} is {self.n*self.n}")
    
    def cube(self):
        print(f"The cube of {self.n} is {self.n*self.n*self.n}")
    
    def sq_root(self):
        print(f"The square root of {self.n} is {self.n**(1/2)}")

p = calculator(4)
p.square()
p.cube()
p.sq_root()