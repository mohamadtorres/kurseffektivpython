# 2.1 3. Decorator med flera niv˚aer
# Skapa en decorator som r¨aknar hur m˚anga g˚anger en funktion anropas

namn_lista = ["Mohammad", "Rihana", "Fatema", "AFI"]

def counter_logg(func):
    counter = 0 
    def wrapper(*args,**kwargs):
        nonlocal counter
        counter += 1
        print(f"Funcktionen anropades {counter} gånger")
        return func(*args,**kwargs)
        
        

    return wrapper


@counter_logg
def say_hello(lista:list):
    for namn in lista:
        print(f"Hello {namn}")

say_hello(namn_lista)
say_hello(namn_lista)
say_hello(namn_lista)
say_hello(namn_lista)
