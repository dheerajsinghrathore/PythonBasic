user_input = input("Enter 5 number: ")
my_list = [int(ch) for ch in user_input.split()]
print(sum(my_list))