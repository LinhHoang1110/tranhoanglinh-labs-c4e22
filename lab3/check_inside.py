# from inside import *

def is_inside(p=[], l=[]):
    if l[0] <= p[0] <= l[2] + l[0] and l[1] <= p[1] <= l[1] + l[3]:
        return True
    else:
        return False

check_inside = is_inside([100, 120], [140, 60, 100, 200])  

if check_inside == False:
    print("Your function is correct")
else: 
    print("Oops, there's a bug")    