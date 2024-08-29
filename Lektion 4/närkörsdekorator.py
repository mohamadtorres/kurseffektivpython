print("Start")
print("*"*20)

def the_one_decorator(func):
    print("the_one_decorator runs!")
    def wrapper(*args,**kwargs):
        print("Wrapper starts!")
        val = func(*args, **kwargs)
        print("Wrapper Ends!")
        return val
    return wrapper


print("Something")
print("*"*20)

@the_one_decorator
def the_one_and_only_func(*args,**kwargs):
    print("The function runs!")
    print(f"The arguments were {args} and keys are {kwargs}")
    print("The function ends!")


print("*"*20)
print("          Program start          ")
print("*"*20)
the_one_and_only_func(1,2,3,hello="Hejsan",goodbye = "Hejdå!")
print("*"*20)
the_one_and_only_func()
print("*"*20)
