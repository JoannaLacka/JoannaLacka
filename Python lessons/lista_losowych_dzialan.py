import random

def stworz_dzialanie():
    liczba1 = random.randrange(1,21)
    liczba2 = random.randrange(6,31)
    return f"{liczba1} + {liczba2} = "

for i in range(1,11):
    print(stworz_dzialanie())