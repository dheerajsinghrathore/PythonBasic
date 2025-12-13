f = None
try:
    f = open(
        "/Users/dheerajrathore/Documents/GenAIPython By SCA/file_read_write/message.txt",
        "r",
    )
    lines = 0
    while True:
        text = f.readline()
        if text == "":
            break
        print(text.strip())
        lines += 1
    print("Total lines read:", lines)
except FileNotFoundError as ex1:
    print("Cannot create the file", ex1)
except OSError as ex2:
    print("Cannot read the data", ex2)
finally:
    if f is not None:
        f.close()
        print("File closed successfully")
