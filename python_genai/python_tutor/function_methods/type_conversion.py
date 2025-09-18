a = 10
b = 1.5
c= a + b
print(c)  # 11.5
print(type(c))  # <class 'float'>
d = 4
e = True
print(d + e)  # 5 (True is treated as 1)
print(type(d + e))  # <class 'int'>
f = 10
g = "20"
#print(f + g)  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(f + int(g))  # 30
print(str(f) + g)  # 1020
print(int("Dheraj"))  # ValueError: invalid literal for int() with base 10: 'Dheeraj'
print(float("Dheraj"))  # ValueError: could not convert string to float: 'Dheeraj'
print(float("10.5"))  # 10.5
print(int("10.5"))  # ValueError: invalid literal for int() with base 10: '10.5'
print(int("100") + int("200"))  # 300
print(float("1.5") + float("2.5"))  # 4.0
print(int(2.9))  # 2 (truncates the decimal part)
print(float(5))  # 5.0
print(int(True))  # 1
print(int(False))  # 0
print(float(True))  # 1.0
print(float(False))  # 0.0
print(str(True))  # 'True'
print(str(False))  # 'False'
print(str(100))  # '100'
print(str(1.5))  # '1.5'
print(bool(1))  # True
print(bool(0))  # False
print(bool(-1))  # True
print(bool(0.0))  # False
print(bool(0.1))  # True
print(bool(""))  # False
print(bool("Hello"))  # True
print(bool(" "))  # True (non-empty string)
print(bool([]))  # False (empty list)
print(bool([1, 2, 3]))  # True (non-empty list)
print(bool(()))  # False (empty tuple)