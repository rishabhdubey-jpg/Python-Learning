a = 89

def fun():
    global a
    a = 3
    print(a)

fun()
print(a)

'''
THE GLOBAL KEYWORD
'global' keyword is used to modify the variable outside of the current scope.

'''