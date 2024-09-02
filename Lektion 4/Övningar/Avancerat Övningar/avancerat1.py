# Skapa en lista med alla kvadrater av j¨amna tal fr˚an 1 till 100 som ¨ar
# delbara med 4 men inte med 8.

lista = [num ** 2 for num in range (1,101) if num % 4 == 0 and num % 8 != 0]
print(lista)
print("*" * 15)
#Skapa ett set med de f¨orsta bokst¨averna av orden i listan ["Python","is", "powerful", "and", "fun"] d¨ar ordet har mer ¨an tre bokst¨aver.

lista = ["Python","is", "powerful", "and", "fun"]
ny_set = {ord[0] for ord in lista if len(ord) > 3}
print(ny_set)

print("*" * 15)
# Skapa en dictionary d¨ar nycklarna ¨ar orden i meningen "Python comprehensions
# are powerful" och v¨ardena ¨ar orden bakl¨anges

sträng = "Python comprehensions are powerful"
lista = sträng.split()
dict1 = {k:k[::-1] for k in lista}
print(dict1)