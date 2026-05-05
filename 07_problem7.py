# Write a program to print the following star pattern.
'''

  *
 ***
***** for n = 3

'''

n = int(input("Enter the number: "))
for i in range(1, n+1):
    print(" "* (n-i), end="")    # (n-i) for the spaces before the star on every line, and (, end="") is for not taking a new line as from default print statement.
    print("*"* (2*i-1), end="")  # (2*i-1) is a series of odd numbers.
    print("")                    # For the new line.