# A tuple is an immutable data type in python.

a = ()          # empty tuple
# b = (1)       # indicates an assignment to the variable b of integer 1.
b = (1,)        # tuple with only one element needs a comma.
c = (1,7,2)     # tuple with more than one element.
print(type(a))
print(type(b))
print(type(c))

d = (11, 77, "rishabh", 45.07, True, None, "Sourabh")
print(d)
# d[0] = 4533     # we cannot change a tuple, because it is immutable.