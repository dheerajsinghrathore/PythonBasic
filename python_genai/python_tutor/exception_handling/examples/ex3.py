a=input("Enter first number")
b=input("Enter second number")
a=int(a)
b=int(b)
try:
    div=a/b
    print("division of",a,"and",b,"is",div)
except(ZeroDivisionError):
    print('Please do not input 0 as denominator')
except(ValueError): # This except block will never run
    print('Please input digts only')
sum=a+b
print("Sum of",a,"and",b,"is",sum)