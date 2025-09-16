str1 = 'Hello' \
'' \
' World'
print(str1)
#Slicing
str2 = "Bhopal"
print(str2[0:3])  # 'Bho'
print(str2[1:5])  # 'hopa'
print(str2[:4])   # 'Bhop'
print(str2[2:])   # 'opal' # 'opal'
print(str2[-4:-1]) # 'opa'
print(str2[-1:-4]) # '' (empty string)
print(str2[-4:])   # 'opal'
print(str2[:])     # 'Bhopal'
print(str2[::2])   # 'Bpa' (every second character)
print(str2[1::2])  # 'hopl' (every second character starting from index 1)
print(str2[::-1])  # 'lapohB' (reversed string)
print(str2[::3])   # 'Bol' (every third character)
print(str2[2:2])  # '' (empty string)

str3 = "Hello"
print(str3[6:10])  # '' (empty string, no error)
print(str3[-2:2])  # '' (empty string, no error)
print(str3[18:15]) # '' (empty string, no error)
print(str3[2])     # IndexError: string index out of range