f = None
try:
    f = open(
        "/Users/dheerajrathore/Documents/GenAIPython By SCA/file_read_write/sample.txt",
        "r",
    )
    my_list = f.readlines()
    for str in my_list:
        print(str.strip())
    print("Total lines read:", len(my_list))
except FileNotFoundError as ex1:
    print("Cannot create the file", ex1)
except OSError as ex2:
    print("Cannot read the data", ex2)
finally:
    if f is not None:
        f.close()
        print("File closed successfully")
