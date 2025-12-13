f = None
try:
    f = open("msg.txt", "a+")
    f.seek(0)
    data = f.read()
    print("File Data:", data)
    f.seek(-1, 2)
except FileNotFoundError:
    print("Cannot create the file")
except OSError as ex:
    print("Error:", ex)
finally:
    if f is not None:
        f.close()
        print("File closed")
