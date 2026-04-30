# If else and Elif statements are a multiway decision taken by our program due to certain
# conditions in our code.

a = int(input("Enter your age: "))

# If elif else ladder
if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("You are entering an invalid negative age")

elif(a == 0):
    print("You are entering 0 which is not a valid age")

else:
    print("You are below the age of consent")

print("End of Program")

# if(a>=18):
#(   )print("You are above the age of consent")
#(   )print("Good for you")
#  ^
#  |
#  |
#{indent} this space is called indent, which means we are inside the condition here.

# 1. There can be any number of Elif statements.
# 2. Last else is executed only if all the conditions inside Elits fail.