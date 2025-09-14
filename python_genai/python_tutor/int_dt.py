import sys
a=10    #decimal number syntax
b=0b1010  #binary number syntax
c=0o12    #octal number syntax
d=0xA     #hexadecimal number syntax
print(a,b,c,d)
print(type(a),type(b),type(c),type(d))
print(id(a),id(b),id(c),id(d))
print(sys.getsizeof(a),sys.getsizeof(b),sys.getsizeof(c),sys.getsizeof(d))
#All are of int datatype
#All are of same size in memory
#All have different memory address
#All are of same value
#All are of same type
#All are immutable