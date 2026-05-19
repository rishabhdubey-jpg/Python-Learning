from functools import reduce
# Map Example
l = [1, 2, 3, 4, 5]

square = lambda x: x*x

sqList = map(square, l)
print(list(sqList))

# Filter Example
def even(n):
    if (n%2 == 0):
        return True 
    return False

onlyEven= filter(even, l)
print(list(onlyEven))

# Reduce Example
def sum(a, b):
    return a + b

mul = lambda x, y: x*y

print(reduce(sum, l))
print(reduce(mul, l))

'''
MAP, FILTER & REDUCE
Map applies a function to all the items in an input_list.

Syntax.
map(function, input_list)
# the function can be lambda function

Filter creates a list of items for which the function returns true.

list(filter(function))
# the function can be lambda function

Reduce applies a rolling computation to sequential pair of elements.

from functools import reduce
val=reduce (function, list1)
# the function can be lambda function

'''