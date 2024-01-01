# klasa deifinuje obiekt. klasa jest instrukcją tworzenia obiektów, nazwy klas powinny byc tworozne w postaci rzeczownika i rozpoczynać się z wielkiej litery

class Osoba:
    liczba_osob = 0
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek
        Osoba.liczba_osob +=1

    def wyswietl_dane_osobowe(self):
        print(f"Imię: {self.imie}, wiek: {self.wiek}")

    @staticmethod
    def wyswietl_ilosc_osob():
        print("Liczba wszystkich osób: ", Osoba.liczba_osob)

osoba1 = Osoba("Ania",23 )
# print(osoba1.imie)
# print(osoba1.wiek)
osoba1.wyswietl_dane_osobowe()

# metoda statyczna dotyczy sie calej klasy
Osoba.wyswietl_ilosc_osob()