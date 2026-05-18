try:
    a = int(input("Hey, Enter a number: ") )
    print(a)

except Exception as e:
    print(e)

else:
    print("I am inside the else.")

print("Thank You")

'''
TRY WITH ELSE CLAUSE
Sometimes we want to run a piece of code when try was successful.

try:
# Somecode
except:
# Somecode
else:
# Code          # This is executed only if the try was successful

'''