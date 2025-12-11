try:
    f = open()
    str = input("Enter file name: ")
    f.write(str)
except(FileNotFoundError, IOError) as e:
    print("An error occurred:", e)
    print("File not found or IO error.") 