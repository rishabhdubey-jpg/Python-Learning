def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("Hey I am inside of finally")

main()

'''
TRY WITH FINALLY
Python offers a 'finally' clause which ensures execution of a piece of code inspective of the exception.
It is effective in the function, shown in the above example if it returns.

try:
# Some Code
except:
# Some Code
finally:                # Executed regardless of error!
# Some Code

'''