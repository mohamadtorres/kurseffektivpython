# Caching med decorators
# Skapa en decorator som cachar resultatet av en funktion f¨or att f¨orb¨attra prestanda


def cache ( func ):
    cached_results = {}

    def wrapper (* args ):
        if args in cached_results :
            print ("Hämtar från cache ")
            return cached_results [ args ]
        result = func (* args )
        cached_results [ args ] = result
        return result
    return wrapper

@cache
def slow_function (x ):
# Simulerar en l˚a ngsam operation
    from time import sleep
    sleep (2)
    return x * x

print ( slow_function (4))
print ( slow_function (4)) 