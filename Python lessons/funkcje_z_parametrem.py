# parametry domyślne są na końcu, a te parametry zmienne są pierwsze
def wyswietl_powitanie(imie, powitanie = "Hej"):
    print(powitanie, imie)


wyswietl_powitanie("Adam")
wyswietl_powitanie("Adam","Cześć")


wyswietl_powitanie("Jola")
wyswietl_powitanie("Mati", "Dzień dobry")
wyswietl_powitanie("Asia")


