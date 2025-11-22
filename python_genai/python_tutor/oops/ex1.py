class Emp:
    pass

e1 = Emp()
e2 = Emp()
print(type(e1))
print(type(e2))
print(id(e1))
print(id(e2))
print(e1 == e2)
print(e1 is e2)
print(Emp == Emp)
print(Emp is Emp)