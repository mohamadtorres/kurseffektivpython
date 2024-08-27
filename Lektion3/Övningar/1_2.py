# 1.2 2. Decorator med argument
# Skapa en decorator som skriver ut namnet p˚a den funktion som anropas samt de argument som
# skickas in till funktionen.

def dekorator(func):
    def wrapper(*args, **kwargs):
        
        print(f"Functionen heter {func.__name__}")
        print(f"functionen tar {args} and {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@dekorator
def add(a,b):
    return a + b

print(add(6,9))