a=input("Enter first number")
b=input("Enter second number")
try:
    a=int(a)
    b=int(b)
    div=a/b
    print("division of",a,"and",b,"is",div)
except (ValueError):
    print("Please do not input non numeric data")
except(ZeroDivisionError):
    print('Please do not input 0 as denominator')