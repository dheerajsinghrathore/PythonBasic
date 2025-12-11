class InvlidNumberError(Exception): # programmer defined excep, custom except
    pass
while True:
    try:
        a=int(input("enter numerator:"))
        b=int(input("enter denominator:"))
        if a<=0 or b<0:
            raise InvlidNumberError("Negative values or 0 not allowed")
        div=a/b
        print("Div is",div)
    except (ValueError)as ex1:
        print("Only int inputs allowed")
    except (ZeroDivisionError)as ex2:
        print("Denominator must not be 0")
    except (InvlidNumberError) as ex3:
        print(ex3)
    else:
        break
       