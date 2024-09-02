# Filtrera ut alla ord i listan ["apple", "banana", "cherry", "date"]
# som inneh˚aller bokstaven ”a”

listan = ["apple", "banana", "cherry", "date"]
ny_lista = [ord for ord in listan if "a" in ord]
print(ny_lista)