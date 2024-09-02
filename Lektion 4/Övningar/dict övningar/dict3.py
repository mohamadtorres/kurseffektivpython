#Givet dictionaryt "a": 1, "b": 2, "c": 3, skapa ett nytt dictionary d¨ar v¨ardena ¨ar kvadraterna av de ursprungliga v¨ardena

dict1 = {"a": 1, "b": 2, "c": 3}
nydict = {k:dict1[k] ** 2 for k in dict1}

print(nydict)