# przyklad programu ktory sprawdza czy z podanych dlugosci mozna zbudowac trojkat
# warunek aby zbudowac trojkat suma 2 krotszych bokow musi byc wieksza od najdluzszego boku

def pobierz_boki_trojkata():
    boki_trojkata = []
    try:
        for i in range(1,4):
            bok = float(input(f"Bok nr {i}: "))
            boki_trojkata.append(bok)
        boki_trojkata.sort()
        
        if(boki_trojkata[0] > 0):
            sprawdz_czy_mozna_zbudowac_trojkat(boki_trojkata)
        else:
            print("Boki muszą być większe od 0")
    except:
        print("Podaj długości boków w postaci liczby")

def sprawdz_czy_mozna_zbudowac_trojkat(boki):
    if(boki[2] < (boki[0] + boki[1])):
        print("Można zbudować trójkąt o podanych bokach")
        print(f"Obwód trójkąta wynosi: {sum(boki)}")
    else:
        print("Nie można zbudować trójkąta")

pobierz_boki_trojkata()