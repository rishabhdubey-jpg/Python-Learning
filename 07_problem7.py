# If the names of 2 friends are same; what will happen to the program in problem 6?

d = {}

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

print(d)

# Because of the update func, the recently added lang is the final fav lang for that name, and the older one will be removed from the dictionary.