def show():
    b = 20
    print("Inside show():", b)

show()
print("Outside show():", b)  # This will raise an error because 'b' is not defined in this scope