# Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce

def greater(a, b):
    if(a>b):
        return a
    return b

l = [5, 3, 555, 40, 23, 98, 450, 6463]

print(reduce(greater, l))