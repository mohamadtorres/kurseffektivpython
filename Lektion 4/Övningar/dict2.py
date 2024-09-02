#Skapa en dictionary fr˚an listan ["apple", "banana", "cherry"] d¨ar varje nyckel ¨ar ett ord och v¨ardet ¨ar l¨angden p˚a ordet.
listan = ["apple", "banana", "cherry"]
ny_dict = {ord:len(ord) for ord in listan }
print(ny_dict)