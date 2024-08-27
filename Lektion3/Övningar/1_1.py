# 1.1 1. Skapa en enkel decorator
# Skapa en decorator som skriver ut ’F¨ore funktionen’ innan en funktion k¨ors och ’Efter funktionen’
# efter att funktionen har k¨orts


def dekorator(func):
    def wrapper():
        print("Före functionen")
        func()
        print("Efter functionen")
    return wrapper

@dekorator
def say_hello():
    print("Hej på dig!")


say_hello()


#inja aval bedune wrapper sakhte budam. dekorator bedune wrapper nemishe 