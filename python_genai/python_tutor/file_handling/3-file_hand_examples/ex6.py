f = None
try:
    f = open("msg.txt", "r+")
    data = f.read()
    print(data)
    f.seek(0)
    f.write("Hello\n")
    f.write("From\n")
    f.seek(0)
    data = f.read()
    print(data)
except FileNotFoundError:
    print("Cannot create the file")
except OSError as ex:
    print("Error:", ex)
finally:
    if f is not None:
        f.close()
        print("File closed")
