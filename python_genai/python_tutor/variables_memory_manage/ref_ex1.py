import sys
a=  100
b = 100
print(a is b)  # True, same object for small integers
print(id(a), id(b)) # Same id

c = 300
d = 300
print(sys.getrefcount(a))