# If languages of two friends are same; what will happen to the program in problem 6?

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

# In the dictionaries, a key is a identifier so it cannot me same, it will be updated, but values of any two keys can be same without any problem.