# slowniki róznią sie od zwykłej listy tym ze w listach operujemy na numerze indesksu, a w słownikach odwołujemy się za pomocą klucza

dane_osobowe = {
    "imie" : "Ania",
    "wiek" : 36,
    "wzrost" : 160
}

dane_osobowe["wzrost"] = 180

# print(dane_osobowe)
# print(list(dane_osobowe.keys()))
print(list(dane_osobowe.values()))

# tworznie słownika
a = {}
print(type(a))