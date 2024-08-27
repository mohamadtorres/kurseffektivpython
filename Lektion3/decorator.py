def första(func):
    def wrapper():
        print("Första körs")
        return func()
    return wrapper

def andra(func):
    def wrapper():
        print("Andra körs")
        return func()
    return wrapper

@första
@andra
def say_hello():
    print("Hello!")


say_hello()