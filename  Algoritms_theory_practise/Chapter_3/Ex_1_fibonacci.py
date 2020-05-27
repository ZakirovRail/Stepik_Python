def fib1(n):
    assert n >= 0
    return n if n <= 1 else fib1(n - 1) + fib1(n - 2)
#
#
# print(fib1(8))
# print(fib1(15))
# print(fib1(10))
#--------------------------------------------------------------------------------------------------

cache = {}
def fib2(n):
    assert n >=0
    if n not in cache:
        cache[n] = n if n <= 1 else fib2(n-1) + fib2(n-2)
    return cache[n]


# print(fib2(8))
# print(cache)
# print(fib2(18))
# print(cache)
# print(fib2(800))
#--------------------------------------------------------------------------------------------------

def memo(f):
    cache = {}
    def inner(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return inner

#--------------------------------------------------------------------------------------------------
from functools import lru_cache

fib1 = lru_cache(maxsize=None)(fib1) # analog of memo
# print(fib1(499)) # 86168291600238450732788312165664788095941068326060883324529903470149056115823592713458328176574447204501



#--------------------------------------------------------------------------------------------------
def fib3(n):
    assert n >=0
    f0, f1 = 0, 1
    for i in range(n -1):
        f0, f1 = f1, f1 + f0
    return f1

print(fib3(80000))






