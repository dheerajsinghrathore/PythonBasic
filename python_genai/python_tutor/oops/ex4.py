class Emp:
    def __init__(self, age, name, salary):
        self.age = age
        self.name = name
        self.sal = salary

e1 = Emp(32, "Dheeraj", 50000)
print("age:", e1.age, "name:", e1.name, "salary:", e1.sal)
e2 = Emp(28, "Rathore", 60000)
print("age:", e2.age, "name:", e2.name, "salary:", e2.sal)
