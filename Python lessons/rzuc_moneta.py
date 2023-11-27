import random

def rzuc_moneta():
    losowa = random.randrange(0,2)
    if(losowa == 1):
        return "orzel"
    else:
        return "reszka"
    
print(rzuc_moneta())
