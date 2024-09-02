#Skapa en dictionary d¨ar nycklarna ¨ar talen fr˚an 1 till 5 och v¨ardena ¨ar kvadraterna av dessa tal.

ny_dict = {num:num ** 2 for num in range(1,6)}
print(ny_dict)