# Unika bokst¨aver: Givet listan ["apple", "banana", "avocado"],
# skapa ett set av alla unika bokst¨aver som f¨orekommer i n˚agot av orden.


lista = ["apple", "banana", "avocado"]
nyset = {bokstav for ord in lista for bokstav in ord}

print(nyset)
# listajadid = []
# for ord in lista:
#     for letter in ord:
#         if letter not in listajadid:
#             listajadid.append(letter)

# print(set(listajadid))


#======================================¨

# Multiplar: Skapa ett set med alla tal fr˚an 1 till 100 som ¨ar multiplar
# av b˚ade 3 och 5.

ny_set = {nummer for nummer in range(1,101) if nummer % 3 == 0 and nummer % 5 == 0}
print(ny_set)


#===================
# Konsonanter: Givet en str¨ang "comprehensions are cool", skapa
# ett set med alla unika konsonanter

sträng = "comprehensions are cool"
konsonanter= "bcdfghjklmnpqrstvwxz"
ny_set1 = {konsonat for konsonat in sträng if konsonat in konsonanter}
print(ny_set1)