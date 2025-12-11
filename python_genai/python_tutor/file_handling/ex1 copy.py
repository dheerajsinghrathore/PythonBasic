try:
    f=open("g:/message.txt","w")
    str=input("Type something:")
    f.write(str)
except(FileNotFoundError)as ex1:
    print("Cannot create the file",ex1)
except(OSError)as ex2:
    print("Cannot write the data",ex2)
finally:
    f.close()
    print("File saved successfully")    