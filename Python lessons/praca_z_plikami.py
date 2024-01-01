# otwieranie plików do odczytu i zapisu przebiega za pomocą metody open(), która przyjmuje pewne argumenty: ściezkę dostępu do pliku i sposób pracy na pliku.

# mozemy otworzyć plik:
# r- tylko do odczytu (read), plik musi istnieć i znajdować się w podanej lokalizacji
# a - dodanie zawartości (append), mozna dodać coś do isniejącego pliku, w przypadku jesli plik nie istnieje w podanej lokalizacji, zostanie utworzony od nowa
# w - zapisać coś od nowa (write) plik zostanie wyczyszczony i zapisany nową wartoscią. W przypadku jeśli plik nie istnieje w podanej lokalizacji, zostanie utworzony od nowa.

# mozemy sprecyzować czy plik jest zwykłym plikiem tesksowym (t) czy binarnym, np grafiką (b)

# po zakończeniu pracy na plikach powinny one zostać zamknięte za pomocą metody close()

# file = open("plik.txt", "a")
# file.write("python")
# file.write("\n")
# file.close()


with open("plik.txt", "a") as file:
    file.write("python next")
    file.write("\n")

import os
if os.path.exists("plik.txt"):
    with open("plik.txt", "r") as file:
        print(file.read())

        # for line in file:
        # print(line)
