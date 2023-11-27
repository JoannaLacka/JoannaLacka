# for i in range(10,21,3):
    # print(i)

# przykład uzycia pętli for do wypisania liczb od 1 do 10 w jednym wierszu, oddzielonych przecinkiem
# >> 1,2,3,4,5,6,7,8,9,10

liczby = ""
for i in range(1,11):
    liczby += str(i) + ","

# print(liczby[:-1])

liczby = ""
for i in range(10,0,-1):
    liczby += str(i) + ","

print(liczby[:-1])
