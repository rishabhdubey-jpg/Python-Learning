# Dictionary is a collection of keys-value pairs.

# Syntax:

# a= {"key":"value",
# "harry":"code",
# "marks":"100"
# "list":[1,2,9]
# }

# a["key"] # prints "value"
# a[list] # prints [1,2,9]

# PROPERTIES OF PYTHON DICTIONARIES

# 1. It is unordered.
# 2. It is mutable.
# 3. It is indexed.
# 4. Cannot contain duplicate keys.

d = {}  # Empty Dictionary
marks = {
"Rishabh": 100,
"Krishna": 56,
"Sourabh": 23,
0: "Rishabh"

}

print(marks, type(marks))
print(marks["Rishabh"])
print(marks[0])