def add(x,y):
    r = x + y
    return r

# a = int(input("a = "))
# b = int(input("b = "))

# t = add(a,b)    
# print(t)
from random import choice

def eval(x,op,y):
    if op == "+":
        return x + y
    elif op == "-":
        return x - y    
    elif op == "*":
        return x*y
    elif op == "/":
        return x/y    


