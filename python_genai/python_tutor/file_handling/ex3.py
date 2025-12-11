a=10
b=20
def show():
    x=5
    y=7
    print(locals())
    print('x' in locals())
show()
print(globals())
print('a' in globals())
