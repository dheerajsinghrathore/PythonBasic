x=10
def show():
    y = x + 5
    print("Inside show():", x)

show()
print("Outside show():", x)  # This will print 10 because 'x' is not modified globally