def add(*x):
    print("Sum is:", sum(x))
    print(type(x))

add(2, 3)
add(2, 3, None, "Hello")
add(2, 3, 4, 5)