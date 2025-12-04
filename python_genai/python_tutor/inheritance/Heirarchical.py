class Polygon:
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    def __str__(self):
        return f"Polygon with dimensions ({self.dim1}, {self.dim2})"
    
class Rectangle(Polygon):
    def area(self):
        return self.dim1 * self.dim2
    
class Square(Polygon):
    def area(self):
        return self.dim1 * self.dim1

rect = Rectangle(4, 5)
print(rect)                  # Output: Polygon with dimensions (4, 5)
print("Rectangle Area:", rect.area())  # Output: Rectangle Area: 20 