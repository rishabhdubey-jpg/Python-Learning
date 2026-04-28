marks = {
"Rishabh": 100,
"Krishna": 56,
"Sourabh": 23,
0: "Rishabh"
}

print(len(marks))                   # Returns the length of a dictionary.

# print(marks)
# print(marks.items())              # Returns a list of (key,value)tuples.
# print(marks.keys())               # Returns a list containing dictionary's keys.
# print(marks.values())             # Returns a list containing dictionary's values.
# marks.update({"Rishabh": 99, "Shristi": 100})    # Updates the dictionary with supplied key-value pairs.

# print(marks.get("Rishabh"))     # Returns the value of the specified keys (and value is returned eg."Rishabh" is returned here).
# print(marks.get("Rishabh2"))    # Prints None
# print(marks["Rishabh2"])        # Returns an error

# value = marks.pop('Sourabh', '23')  # Removes the specified key and returns the corresponding value. 
# print(value)
# value1 = marks.pop('Sourabh2')      # If the key is not found, "default" is returned if provided, otherwise "KeyError" is raised.
# print(value1)


# dict.popitem() : Removes and returns a (key, value) pair from the dictionary. Pairs are returned in LIFO (last-in, first-out) order.
# item = marks.popitem()
# item1 = marks.popitem()
# print(item)
# print(item1)

print(marks)
