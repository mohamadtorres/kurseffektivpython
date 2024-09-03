# Invertera dictionary: Givet dictionaryn "a": 1, "b": 2, "c":
# 3, "d": 4, skapa en ny dictionary d¨ar nycklarna ¨ar de ursprungliga
# v¨ardena och v¨ardena ¨ar de ursprungliga nycklarna. Om det finns du-
# plicerade v¨arden i den ursprungliga dictionaryn, anv¨and en lista av
# nycklar som v¨arde

dict1 = {"a": 1, "b": 2, "c": 3, "d": 4}
nydict = {värde:nyckel for nyckel,värde in dict1.items()}
print(nydict)


#=====================

# Frekvens av n-gram: Givet en textstr¨ang, skapa en dictionary d¨ar
# nycklarna ¨ar alla m¨ojliga 3-gram (sekvenser av tre bokst¨aver) och v¨ardena
# ¨ar frekvensen av varje 3-gram i str¨angen

sträng = "Mohammad Khavari dele mano bordi"
ren_sträng = sträng.replace(" ", "")
nydict1 = {ren_sträng[i:i+3]:ren_sträng.count(ren_sträng[i:i+3]) for i in range(len(ren_sträng)-2)}

print(nydict1)


#===============
# Ord till bokstavssumma: Skapa en dictionary fr˚an en lista av ord
# d¨ar varje nyckel ¨ar ett ord och v¨ardet ¨ar summan av bokst¨avernas
# positioner i alfabetet (t.ex. ’a’ = 1, ’b’ = 2, etc.).

