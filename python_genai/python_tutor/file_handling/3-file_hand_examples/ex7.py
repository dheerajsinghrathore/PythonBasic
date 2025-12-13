f = None
try:
    f = open("msg.txt", "w+")
    data = f.read()
    print("Initial data:")
    print(data)
    f.write("Gen AI\n")
    f.write("is an essesntial skill today")
    f.seek(0)
    data = f.read()
    print("After changing:")
    print(data)
except FileNotFoundError:
    print("Cannot create the file")
except OSError as ex:
    print("Error:", ex)
finally:
    if f is not None:
        f.close()
        print("File closed")
