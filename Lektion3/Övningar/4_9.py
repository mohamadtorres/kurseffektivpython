# Decorator f¨or att logga funktionens exekveringstid med varning
# vid l˚angsam k¨orning
# Skapa en decorator som loggar exekveringstiden f¨or en funktion och ger en varning om funktionen
# tar l¨angre tid ¨an en specificerad gr¨ans att k¨ora



import time
from timeit import default_timer

def warning_slow_func(stakeholder):
    def decorator(func):
        def wrapper(*args,**kwargs):
            start_tid = default_timer()
            func(*args,**kwargs)
            end_tid = default_timer()
            skillnad = end_tid - start_tid
            if skillnad > stakeholder:
                print(f"Warning!!! Functionen {func.__name__} tog {end_tid - start_tid:.2f} som är längre än {stakeholder} som var angiven")
            else:
                print(f"Functionen {func.__name__} tog {end_tid - start_tid:.2f} som är kortare än {stakeholder} som var angiven")
        return wrapper
    return decorator


@warning_slow_func(3)
def slow_function():
    time.sleep(1.5)
    #sleep gör en försening (sleep) INNAN programmet anropas

slow_function()