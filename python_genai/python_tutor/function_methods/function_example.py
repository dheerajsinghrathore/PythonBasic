city = "Bhopal"
print(city.upper())  # BHOPAL
print(len(city))    # 6
print(city.lower())  # bhopal
print(city.capitalize())  # Bhopal
print("Bhoapal" > "Bhipappa")   # True (lexicographical comparison  based on ASCII values)
print("Bhoapal" < "Bhipappa")
print("amit" > "AMIT")
print("amit" < "AMIT")
print(city.replace("Bho", "Mho"))  # Mhopal
print(city.find("pal"))  # 3
print(city.find("xyz"))  # -1
print(city.count("p"))  # 2
print(city.startswith("Bho"))  # True
print(city.endswith("pal"))  # True
print(city.split("o"))  # ['Bh', 'pal']
print(city.isalpha())  # True
print(city.isdigit())  # False
print(city.index("pal"))  # 3
# print(city.index("xyz"))  # ValueError: substring not found
print(city.center(20, '*'))  # *******Bhopal********
print(city.ljust(20, '-'))  # Bhopal--------------
print(city.rjust(20, '-'))  # --------------Bhopal
print(city.strip("al"))  # Bhop
