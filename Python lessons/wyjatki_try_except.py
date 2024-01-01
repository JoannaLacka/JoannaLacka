cena = input("Podaj cenę przed obnizką: ")
obnizka = input("Wartość procentowa obnizki: ")
try:
    cena = float(cena)
    obnizka = float(obnizka)
    cena_finalna = cena - (cena * obnizka / 100)
    print("Cena po obniżce = ", cena_finalna)
except:
    print("Nie mozna obliczyc ceny")