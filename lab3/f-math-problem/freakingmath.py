from random import *

from calc import *

def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(0,10)
    y = randint(0,10)
    op = choice(["+","-","*","/"])
    error = randint(-1,1)
    result = eval(x,op,y) + error
    return [x, y, op, result]

def check_answer(x, y, op, result, user_choice):
    if result == eval(x,op,y):
        if user_choice == True:
            return True
        else: 
            return False 
    else:
        if user_choice == True:
            return False
        else:
            return True        


    
