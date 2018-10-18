def is_inside(p=[], l=[]):
    if l[0] <= p[0] <= l[2] + l[0] and l[1] <= p[1] <= l[1] + l[3]:
        return True
    else:
        return False



 




