def bad_range_fun(end:int, infity = False):
    i = 0
    while i <= end or infity:
        yield i
        i += 1

for value in bad_range_fun(10):
    print(value)
print([x for x in bad_range_fun(10)])