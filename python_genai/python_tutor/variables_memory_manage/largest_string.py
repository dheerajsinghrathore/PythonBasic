def findLargestString(*args):
    largest = ""
    for string in args:
        if len(string) > len(largest):
            largest = string
    return largest

result = findLargestString("apple", "banana", "cherrys", "date")
print("The largest string is:", result)