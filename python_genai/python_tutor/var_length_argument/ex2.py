def add(*x):
    sum = 0
    for i in x:
        if isinstance(i, int):
            sum += i
    print("Sum is:", sum(x))
    print(type(x))

add(2, 3)
add(2, 3, None, "Hello")
add(2, 3, 4, 5)