import math
a=input("Enter first number")
b=input("Enter second number")
c=input("Enter power for exp")
try:
    a=int(a)
    b=int(b)
    c=int(c)
    div=a/b
    print("division of",a,"and",b,"is",div)
    res=math.exp(c)
    print("Exp res is",res)
except(ArithmeticError):
    print('power too large')
except (ValueError):
    print("Please do not input non numeric data")
except(ZeroDivisionError):
    print('Please do not input 0 as denominator')
