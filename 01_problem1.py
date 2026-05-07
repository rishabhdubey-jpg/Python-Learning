# Write a program using functions to find greatest of three numbers.

def greatest(a, b, c):
    if(a>b and a>c):
        return a
    
    elif(b>a and b>c):
        return b
    
    elif(c>b and c>a):
        return c

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print(greatest(a, b, c))
