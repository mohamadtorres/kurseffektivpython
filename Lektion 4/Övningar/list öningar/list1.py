# Skapa en lista med kvadrater av alla j¨amna tal fr˚an 0 till 20.

lista = [x ** 2 for x in range (0,21) if x % 2 == 0]
print(lista)