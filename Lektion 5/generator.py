#att använda yield

def fun_func() -> str:
    f = "Hej"
    g = "då"
    ret = f + " " + g
    return ret

def fun_gen():
    f = "Hej"
    yield f
    g = "då"
    yield g
    ret = f + " " + g
    yield ret

print(fun_func())
print(fun_gen())
print(fun_gen())
print(fun_gen())
#<generator object fun_gen at 0x000001ECD6FF8110>
# <generator object fun_gen at 0x000001ECD6FF8110>
# <generator object fun_gen at 0x000001ECD6FF8110

#för att få ett objekt
gen = iter(fun_gen())
print(next(gen)) #gen.__next__()
print(next(gen))
print(next(gen))
