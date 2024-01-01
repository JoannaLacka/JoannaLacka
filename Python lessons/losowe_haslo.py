import random
def generuj_haslo():
    haslo = ""
    for i in range(10):
        losowy_znak = chr(random.randrange(48,123))
        haslo += losowy_znak
    return haslo
print(generuj_haslo())