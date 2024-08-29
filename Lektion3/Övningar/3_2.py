# 5. Decorator med valbara parametrar
# Skapa en decorator som kan ta egna argument, till exempel ett loggningsmeddelande som ska
# skrivas ut varje g˚ang funktionen anropas.

# def dekorator(func, *args, **kwargs):
#     def wrapper(*args,**kwargs):
#         print(f"functionen {func.__name__} körs nu!")
#         func(*args, **kwargs)
#     return wrapper

# @dekorator
# def loggninsmeddelande ():
#     print("Hejsan!")

# loggninsmeddelande()

def log_message ( message ):
    def decorator ( func ):
        def wrapper (* args , ** kwargs ):
            print (f"{ message }: K¨or { func . __name__ } med argument { args }, { kwargs }")
            return func (* args , ** kwargs )
        return wrapper
    return decorator

@log_message (" Anrop till funktionen ")
def multiply (a , b ):
    return a * b



print ( multiply (3 , 4))