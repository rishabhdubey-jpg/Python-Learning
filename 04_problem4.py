# What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?

s = set()
s.add(20)
s.add(20.0)
s.add('20') 
print(s)
print("length =", len(s))

# In Python, comparison operator " == " checks for equality between two values. When comparing
# an integer ('1") and a floating-point number ('1.0"), Python evaluates their values and determines if
# they are numerically equal.
# ( Here integer 20 is equals to floating point number 20.0 )