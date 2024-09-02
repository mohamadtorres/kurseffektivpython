#Omv¨and lista: Skapa en lista med ordens l¨angder i listan ["hello","world", "python"], men i omv¨and ordning


listan = ["hello","world", "python"]

nylista = [len(ord) for ord in listan[::-1]]

print(nylista)


#Summering av siffror: Givet listan [123, 456, 789], skapa en lista som inneh˚aller summan av siffrorna i varje tal.
lista1 = [123, 456, 789]
nylista1 = [sum(int(siffra) for siffra in str(nummer)) for nummer in lista1 ]
print(nylista1)