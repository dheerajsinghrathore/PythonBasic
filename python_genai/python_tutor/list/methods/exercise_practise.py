str = input("Enter a alphanumeric value: ")
digits = []
for char in str:
    if char.isdigit():
        digits.append(char)

print("List of digits in the given alphanumeric value:", digits)
print("Sum of digits:", sum(map(int, digits)))