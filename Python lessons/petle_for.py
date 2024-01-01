# program który losuje 10 liczb od 1 do 10, jezeli zostanie wylosowana 1 petla sie zakonczy
# petla break

import random

for i in range(1,11):
    losowa = random.randrange(1,11)
    if(losowa == 1):
        break
    print(losowa)
