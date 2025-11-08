mylist = []
print("Enter number:")

while True:
    num = int(input("Enter a number : "))
    if num in mylist:
        print("Number already exists in the list. Exiting loop.")
        continue
    mylist.append(num)
    if len(mylist) >= 5:
        break

print("Final list:", mylist)
