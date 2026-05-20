# Write a program to filter a list of numbers which are divisible by 5.
def divisible5(n):
    if(n%5 == 0):
        return True
    return False

l = [5, 3, 555, 40, 23, 98, 450]

f = list(filter(divisible5, l))
print(f)

