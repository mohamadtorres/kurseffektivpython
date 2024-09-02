# 17. Decorator f¨or att konvertera resultatet fr˚an en funktion till en
# viss datatyp
# Skapa en decorator som konverterar resultatet fr˚an en funktion till en viss datatyp, t.ex. str¨ang,
# heltal eller lista
def convert_to(datatype):
    def konvertor_dekorator(func):
        def wrapper(*args,**kwargs):
            result = func(*args,**kwargs)
            return datatype(result)
        return wrapper
    return konvertor_dekorator
@convert_to(str)
def dividera(a,b):
    print(a / b)


dividera(7,2)

#print(type(dividera(7,2)))
#för att vara säker