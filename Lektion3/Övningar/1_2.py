# 1.2 2. Decorator med argument
# Skapa en decorator som skriver ut namnet p˚a den funktion som anropas samt de argument som
# skickas in till funktionen.

def dekorator(func):
    def wrapper():
        
        print(f"Functionen heter {func.__name__}")
        func()
    return wrapper

@dekorator
def say_hello():
    print("Hello motherfucker!")

say_hello()