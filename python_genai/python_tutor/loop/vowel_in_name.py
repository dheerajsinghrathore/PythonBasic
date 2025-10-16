str = input("Enter name to find vowel inside name: ")
i = 0
ch = ''
while i < len(str):
    ch = str[i]
    i += 1
    if ch in 'aeiouAEIOU':
        continue
    print("vowel found:", ch)
else:
    print("consonant")