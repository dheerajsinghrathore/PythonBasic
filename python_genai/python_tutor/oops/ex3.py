class Emp:
    def __init__(myself):
        print(f"Object created with id: {id(myself)}")
        print("self:", myself)

e1 = Emp() 
e2 = Emp()
print("e1:", e1)
print("e2:", e2)