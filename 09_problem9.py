# Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]}

s = {8, 7, 12, "Harry", [1,2]}

s[4][0] = 9

# No, you cannot change the values inside a list contained in a set in Python. In fact, you cannot even
# have a list as an element in a set because sets in Python require all their elements to be immutable
# and hashable. Lists are mutable and not hashable, so they cannot be added to a set.

# If you try to create a set with a list as one of its elements, Python will raise a " TypeError".
