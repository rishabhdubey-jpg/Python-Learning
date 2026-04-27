# Check that a tuple type cannot be changed in python.

a = (223, 45, "Rishabh")

a[2] = "Rdx"    # TypeError: 'tuple' object does not support item assignment, bcuz it is a immutable container