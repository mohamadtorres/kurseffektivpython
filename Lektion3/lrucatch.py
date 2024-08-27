from functools import lru_cache
from timeit import default_timer


@lru_cache(10)
def fib(n):
    match n:
        case 1: return 0
        case 2: return 1
        case _: return fib(n-2) + fib(n-1)


print(fib(14))