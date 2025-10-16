str = input("Enter string: ")
i = 0
while i < len(str):
    if str[i] == 'aeiouAEIOU':
        print("vowel")
        break
    i += 1
else:
    print("consonant")