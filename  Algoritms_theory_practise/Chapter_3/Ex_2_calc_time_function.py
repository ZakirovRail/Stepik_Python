import time


def fib1(n):
    assert n >= 0
    return n if n <= 1 else fib1(n - 1) + fib1(n - 2)


cache = {}
def fib2(n):  #  limitation for maximum recursion which is 499
    assert n >=0
    if n not in cache:
        cache[n] = n if n <= 1 else fib2(n-1) + fib2(n-2)
    return cache[n]


def fib3(n):
    assert n >=0
    f0, f1 = 0, 1
    for i in range(n -1):
        f0, f1 = f1, f1 + f0
    return f1


def timed(f, *args, n_iter=100):
    acc = float('inf')
    for i in range(n_iter):
        t0=time.perf_counter()
        f(*args)
        t1=time.perf_counter()
        acc = min(acc, t1-t0)
    return acc

print('result for fib3 - 8000')
print(timed(fib3, 8000))
print('result for fib2 - 499')
print(timed(fib2, 499))
print('result for fib3 - 80000')
print(timed(fib3, 80000))
