# Function to get ASCII value of a character
def ascii_value(char):
    return ord(char)
print(ord('A'))  # 65
print(ord('a'))  # 97
print(ord('0'))  # 48
print(ord(' '))  # 32
print(ord('@'))  # 64
print(ord('!'))  # 33
print(ord('~'))  # 126
print(ord('\n')) # 10 (newline character)
print(ord('\t')) # 9 (tab character)
print(ascii_value('Z'))  # 90
print(ascii_value('z'))  # 122  