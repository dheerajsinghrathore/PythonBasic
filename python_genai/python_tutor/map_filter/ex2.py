#With map
def square(x):
    return x * x

my_list = [1, 2, 3, 4, 5]
res = map(square, my_list)
print(list(res))  # Output: [1, 4, 9, 16, 25]