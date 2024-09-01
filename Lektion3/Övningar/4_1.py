# Timer Decorator
# Skapa en decorator som m¨ater och skriver ut tiden det tar f¨or en funktion att k¨oras

# from timeit import default_timer


# def timer(func):
#     def wrapper(*args,**kwargs):
#         print(f"Function {func.__name__} körs nu -> {default_timer()}")
#         func(*args,**kwargs)
#         print(f"Function {func.__name__} avslutar nu -> {default_timer()}")
#         return func(*args,**kwargs)

#     return wrapper
    
# @timer
# def function1(x):
#      return (x * x)

    


# print(function1(8))

import time

def timer ( func ):
    def wrapper (* args , ** kwargs ):
        start_time = time . time ()
        result = func (* args , ** kwargs )
        end_time = time . time ()
        print (f"{ func . __name__ } tog { end_time - start_time :.4f} sekunder att köra .")
        return result
    return wrapper

@timer
def compute_square (n ):
    return [x **2 for x in range (n )]

print(compute_square (10000))