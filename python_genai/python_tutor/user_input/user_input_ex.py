import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
circumference = math.tau * radius
print(f"The circumference of the circle with radius {radius} is {circumference:.2f}")
print(f"The area of the circle with radius {radius} is {area:.2f}")