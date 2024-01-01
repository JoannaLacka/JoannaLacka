import random
szukana_liczba = random.randrange(1,101)
odp = 0
ilosc_prob = 0

def podaj_odp():
    global odp
    if(odp == 0):
        tresc_pytania = "Podaj liczbę od 1 do 100: " 
    elif(odp > szukana_liczba):
        tresc_pytania = "Podaj mniejszą liczbę: "
    else:
        tresc_pytania = "Podaj większą liczbę: "
    try:
        odp = int(input(tresc_pytania))
    except:
        print("Podaj wartość numeryczną!")
    global ilosc_prob
    ilosc_prob +=1

while(odp != szukana_liczba):
    podaj_odp()

print(f"Brawo, zgadłeś! Ilość prób: {ilosc_prob}")