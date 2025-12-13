fin = None
fout = None
try:
    fin = open("e:/images/sachin.jpg", "rb")
    fout = open("e:/images/mysachin.jpg", "wb")
    data = fin.read()
    fout.write(data)
except FileNotFoundError as ex1:
    print("Cannot create the file", ex1)
except OSError as ex2:
    print("Cannot read the data", ex2)
finally:
    if fin is not None:
        fin.close()
        print("File closed successfully")
    if fout is not None:
        print("File copied!")
        fout.close()
        print("File closed successfully")
