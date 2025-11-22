class Emp:
    def __init__(self):
        print(f"Object created with id: {id(self)}")
        print("self:", self)

e1 = Emp() 
e2 = Emp()
print("e1:", e1)
print("e2:", e2)