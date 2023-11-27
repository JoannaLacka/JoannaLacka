n = input("Podaj ilość boków: ")
if(n.isnumeric() and int(n) >= 3):
    suma_katow = (int(n)-2) * 180
    print(f"Suma kątów w {n}-boku wynosi: {suma_katow}")
else:
    print("Wprowadzono złą wartość")

# isnumeric sprawdza czy wartośc jest numeryczna pozniej str zamieniamy na int