import random

def generuj_zestaw_liczb_mix(max):
    wszystkie_liczby =[]
    for i in range(0, max):
        wszystkie_liczby.append(i+1)
    random.shuffle(wszystkie_liczby)
    return wszystkie_liczby

def losuj_wygrane_liczby(zestaw_liczb, ilosc_liczb):
    wygrane_liczby = []
    for i in range(0, ilosc_liczb):
        wybrana_liczba = random.randrange(0, len(zestaw_liczb))
        wygrane_liczby.append(zestaw_liczb[wybrana_liczba])
        zestaw_liczb.pop(wybrana_liczba)
    wygrane_liczby.sort()
    return wygrane_liczby

zestaw_wszystkich_liczb = generuj_zestaw_liczb_mix(49)
wygrane_liczby = losuj_wygrane_liczby(zestaw_wszystkich_liczb, 6)
print(wygrane_liczby)
# print(losuj_wygrane_liczby(generuj_zestaw_liczb_mix(49), 6))