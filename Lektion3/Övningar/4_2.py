# # 8. Decorator f¨or att validera inmatning
# # Skapa en decorator som validerar att argumenten som skickas in till en funktion ¨ar av en viss typ.
# # Om fel typ skickas in ska ett undantag kastas.


# def controller(func):
#     def wrapper(*args, **kwargs):
#         if args.isdigit():
#             return func(args)
#         else:
#             return f"Its not a number!"

#     return wrapper

# @controller
# def räknabolån(n):
#     return round(n * 4.4, 2)
#     #eller så ---> return f"{n * 4.4 :.2f}


# test1 = räknabolån(200000)
# print(test1)
# test2 = räknabolån("Mohammad")
# print(test2)

def validate_types ( expected_type ):
    def decorator ( func ):
        def wrapper (* args , ** kwargs ):
            if not all ( isinstance ( arg , expected_type ) for arg in args ):
                raise TypeError (f" Alla argument m˚a ste vara av typen { expected_type . __name__ }")
            return func (* args , ** kwargs )
        return wrapper
    return decorator

@validate_types ( int )
def add_integers (a , b ): return a + b

print ( add_integers (5 , 10)) # Fungerar
print ( add_integers (5 , " 10 " )) # Detta ska kasta ett TypeError