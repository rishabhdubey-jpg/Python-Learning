def greet(name, ending="Thankyou"):
    print(f"Good Dayyy!, {name}")
    print(ending)

greet("Rishabh", "Thanks")
greet("Rohan")

'''
DEFAULT PARMETER VALUE

We can have a value as default as default argument in a function.

If we specify name - "stranger" in the line containing def, this value is used when no
argument is passed.

Example:

def greet(name = "stranger"):
    # function body
greet() # name will be "stranger" in function body (default)
greet("rishabh") # name will be "rishabh" in function body (passed)

'''