# . Decorator f¨or att hantera undantag
# Skapa en decorator som f˚angar upp och hanterar undantag som kan uppst˚a n¨ar en funktion k¨ors

def checker(func):
    def wrapper(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except ZeroDivisionError:
            print("Det går inte dividera med 0")
            
        except Exception as e:
            print(f"Ett fel inträffade: {e}")


    return wrapper


@checker
def dividera(a,b):
    return a / b


print(dividera(25,5))
print(dividera(20,6))
print(dividera(20,0))


