a = 31
p = type(a) # class| <int>

print(p)

b = "31"
q = type (b) # class <str>

print(q)


# str(31)     =>"31"    # integer to string conversion
# int("32")   => 32     # string to integer conversion
# float(32)   => 32.0   # integer to float conversion


c = "31.2"
d = float(c) # c but the type should be float
r = type(d)

print(r)