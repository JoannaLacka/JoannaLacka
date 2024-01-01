#  system kodowania znaków za pomocą liczb
# metoda chr
# znak = 167
# znak = 0x00A7
# znak = 0x1F600
# print(chr(znak))

# # zamiana znaku na liczbę za pomocą metody ord
# znak = '$'
# print(ord(znak))

# generowanie losowego hasła
import random
def generuj_haslo():
    haslo = ""
    for i in range(10):
        losowy_znak = chr(random.randrange(48,123))
        haslo += losowy_znak
    return haslo
print(generuj_haslo())