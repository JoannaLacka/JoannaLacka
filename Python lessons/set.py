my_set = {1, 2, 3, 4, 3, 2, 1, "str", 2.2}
# tworzenie pustego seta
a = set()
print(type(a))

# print(my_set)
# każdy element jest unikatowy, wyprintują się tylko elementy które się NIE POWTARZAJĄ
# elementy seta są: niemutowalne, nie mozna ich zmieniać, nadpisywać, są nieindeksowane i nieuporzadkowane, nigdy nie ma pewnosci w jakiej kolejnosci sa one pobrane. Mozemy dodawac i usuwac elementy.

my_set.add(5)
my_set.discard(2)
# print(my_set)

# mozemy za pomoca seta wyrzucic zduplikowane elementy za pomoca przksztalcenia listy w seta

lista = [4, 6, 6, 7, 8, 8, 4]
new_set = set(lista)

print(new_set)


set_owocowy = {"apple", "banana", "cherry", 12}
lista_owocowa = ["apple", "banana", "cherry", 12]
tuple_owocowy = ("apple", "banana", "cherry", 12)
print(set_owocowy)
print(lista_owocowa)
print(tuple_owocowy)

uczniowie = {"Ania", "Kasia", "Marek", "Zenek"}
kursanci = {"Zosia", "Kasia", "Marek"}
print(uczniowie - kursanci)
# czesc wspólna dwóch ziorów
print(uczniowie & kursanci)
# łączenie zbiorów z wyłączeniem duplikatów
print(uczniowie | kursanci)




