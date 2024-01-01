# metoda split 
tekst = "12-05-2022;22-05-2022;18-06-2022"
rok = tekst.split(';')
for i in range(0,len(rok),1):
    rok[i] = rok[i][-4:]
print(rok)