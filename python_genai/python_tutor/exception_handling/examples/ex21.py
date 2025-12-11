try:
        a=int(input("enter numerator:"))
        b=int(input("enter denominator:"))
        div=a/b
        print("Div is",div)
except (ZeroDivisionError):
        print("Denominator must not be 0")
finally:
        print("Have a good day!")