# JSON to format zapisu i wymiany danych. w tym formacie są pobierane dane ze źródeł zewnętrznych, co umozliwia interakcję programów pisanych w róznych językach lub uzywanych na róznych platformach.

import json

# aDict = {"a":54, "b":87}

# with open("plik1.txt", "w") as file:
#     json_string = json.dumps(aDict, indent = 4)
#     file.write(json_string)

# with open("plik1.txt", "r") as file:
#     slownik = json.loads(file.read())
#     print(slownik)

class Osoba:

    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

# p1 = Osoba("Marian", 36)

# with open("plik.json", "w") as file:
#     json_string = json.dumps(p1.__dict__, indent=4)
#     file.write(json_string)


with open("plik.json", "r") as file:
    osoba = Osoba(**json.loads(file.read()))
    print(osoba.imie, osoba.wiek)