'''
The random-access memory is volatile, and all its contents are lost once a program
terminates in order to persist the data forever, we use files.

A file is data stored in a storage device. A python program can talk to the file by reading
content from it and writing content to it.

TYPE OF FILES.
There are 2 types of files:
1. Text files (.txt, .c ete)
2. Binary files (.jpg. .dat, etc)

'''

f = open("file.txt")
data = f.read()
print(data)
f.close()

'''
Python has a lot of functions for reading, updating, and deleting files.

OPENING A FILE

Python has an open() function for opening files. It takes 2 parameters: filename and mode.

open("filename", "mode of opening(read mode by default)")
open("this.txt", "r")

READING A FILE IN PYTHON
# Open the file in read mode
f = open("this.txt", "r")
# Read its contents
text = f.read()
# Print its contents
print(text)
# Close the file
f.close()
'''