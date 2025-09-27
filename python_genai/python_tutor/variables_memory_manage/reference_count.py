import sys
a = 300
a = 200
print(sys.getrefcount(a))  # Reference count may vary

a = 257
b = 257
print(sys.getrefcount(a))  # Reference count may vary
print(a is b)  # True, same object for small integers
print(id(a), id(b)) # Same id