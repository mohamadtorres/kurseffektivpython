#  Decorator f¨or att sp˚ara hur ofta varje funktion anropas i ett
# program
# Skapa en decorator som h˚aller koll p˚a hur ofta varje funktion i ett program anropas och skriver ut
# statistiken.


lista = [1,2,3,4,5,6,7]


def decorator(func):
    def wrapper(*args,**kwargs):
        counter = 0
        func(*args,**kwargs)
        counter += 1
    return wrapper






def udda(list):
    for i in list:
        if i % 2 == 0:
            print("Jämn")
        else:
            print("Udda!")


udda(lista)