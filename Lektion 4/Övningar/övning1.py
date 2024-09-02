# Filtera och omvandla: Givet en lista med tal [3, 6, 9, 12, 15],
# skapa en ny lista d¨ar varje tal multipliceras med 2 om det ¨ar j¨amnt,
# annars multipliceras med 3


lista = [3, 6, 9, 12, 15]
ny_lista = [num * 2  if num % 2 == 0 else num * 3 for num in lista]
print(ny_lista)
