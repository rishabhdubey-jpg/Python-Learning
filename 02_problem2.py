# Write a python program using function to convert Celsius to Fahrenheit.

def c_to_f(c):
    return (c * (9/5) + 32)

c = int(input("Enter temperature in °C: "))
f = c_to_f(c)
print(f"{round(f, 2)}F")
