import os
try:
        a=int(input("enter numerator:"))
        b=int(input("enter denominator:"))
        div=a/b
        print("Div is",div)
        os._exit(0)#success
except (ZeroDivisionError):
        print("Denominator must not be 0")
finally:
        print("Have a good day!")