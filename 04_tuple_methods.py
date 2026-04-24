a = (1,45,342,3424, False, 45, "Rohan", "Shivam")
print(a)

no = a.count(45)        # returns a count of any element in a tuple
print(no)

i = a.index(3424)       # Return first index of value. Raises ValueError if the value is not present.
print(i)

print(len(a))           # Return the number of items in a container ( tuple ).

# Tuples can be concatenated using the '+' operator.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated = tuple1 + tuple2
print(concatenated) # Output: (1, 2, 3, 4, 5, 6)

# Tuples can be repeated using the '*' operator.
my_tuple = (1, 2, 3)
repeated = my_tuple * 3
print(repeated) # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# You can check if an item exists in a tuple using the 'in' keyword.
my_tuple = (1, 2, 3)
print(2 in my_tuple) # Output: True
print(4 in my_tuple) # Output: False

# Use the 'min()' and 'max()' functions to get the smallest and largest elements in a tuple.
my_tuple = (3, 1,4,2)
print(min(my_tuple)) # Output: 1
print(max(my_tuple)) # Output: 4

# Tuples support slicing to create a new tuple from a subset of the original.
my_tuple = (1, 2, 3, 4, 5)
sliced = my_tuple[1:4]
print(sliced) # Output: (2, 3, 4)

# Tuples can be unpacked into individual variables.
my_tuple = (1, 2,3)
a, b, c = my_tuple
print(a, b, c) # Output: 1 2 3
