# Omv¨and ordlista: Givet en lista ["apple", "banana", "cherry"],
# skapa en dictionary d¨ar nycklarna ¨ar ordens l¨angder och v¨ardena ¨ar
# orden

list1 = ["apple", "banana", "cherry"]

dict1 = {len(ord):ord for ord in list1}
print(dict1)

#============================

# Kvadratr¨otter: Givet en dictionary 1: 1, 4: 16, 9: 81, skapa
# en ny dictionary d¨ar nycklarna ¨ar de ursprungliga nycklarna och v¨ardena
# ¨ar kvadratroten av de ursprungliga v¨ardena
import math
dict2 = {1: 1, 4: 16, 9: 81}
dict3 = {nyckel:math.sqrt(värde) for nyckel,värde in dict2.items() }
print(dict3)

#====================

# Kuber: Skapa en dictionary d¨ar nycklarna ¨ar talen fr˚an 1 till 10 och
# v¨ardena ¨ar kuberna av dessa tal

dict4 = {num:num ** 3 for num in range(1,11)}
print(dict4)