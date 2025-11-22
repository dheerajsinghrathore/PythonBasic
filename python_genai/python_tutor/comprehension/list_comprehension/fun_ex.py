def removeVowels(s):
    my_list = [char for char in s if char.lower() not in 'aeiou']
    return ''.join(my_list)

result = removeVowels("Hello World")
print(result)