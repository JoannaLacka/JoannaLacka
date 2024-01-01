import random
liczba_pkt = 0
ilosc_zadan = 2

def tworz_zadanie():
    liczba1 = random.randrange(1,21)
    liczba2 = random.randrange(1,21)
    tresc_zadania = f"{liczba1} + {liczba2} = "
    odpowiedz = input(tresc_zadania)

    try:
        odpowiedz = int(odpowiedz)
        if(odpowiedz == liczba1 + liczba2):
            global liczba_pkt
            liczba_pkt +=1
    except:
        print("Wynik powinien byc podany w postaci liczby")

for i in range(0, ilosc_zadan):
    tworz_zadanie()

# print(f"Poprawnych odpowiedzi: {liczba_pkt} / {ilosc_zadan}")
print(f"Poprawnych odpowiedzi: {liczba_pkt/ilosc_zadan * 100}%")