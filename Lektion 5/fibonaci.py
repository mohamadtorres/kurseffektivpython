from functools import cache

@cache
def fib(n):
    if n==0: return 0
    if n == 1 : return 1
    return fib(n-1) + fib (n-2)


#testa ett annat sätt


def fib_version2 (n):
    if n==0: return 0
    if n == 1 : return 1
    a,b = 0,1
    step = 2
    while n > step:
        a,b = b, a+b
        yield b
        step += 1

for f in fib_version2(5):
    print(f)