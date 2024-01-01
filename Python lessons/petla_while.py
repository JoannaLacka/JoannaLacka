i = 1
while(i <= 100):
    print(i)
    i += 1

#  powtarzaj komunikat, az zostanie podane prawidlowe haslo

haslo = "1234"
podane_haslo = ""

while(haslo != podane_haslo):
    podane_haslo = input("Podaj hasło: ")

print("Witaj w systemie")
