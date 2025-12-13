f = None
try:
    f = open("msg1.txt", "x")
    str = input("Type something:")
    f.write(str)
except FileNotFoundError as ex1:
    print("Cannot create the file", ex1)
except FileExistsError as ex2:
    print("Error:", ex2)
except OSError as ex3:
    print("Cannot write the data", ex3)
finally:
    if f is not None:
        f.close()
        print("File saved successfully")
