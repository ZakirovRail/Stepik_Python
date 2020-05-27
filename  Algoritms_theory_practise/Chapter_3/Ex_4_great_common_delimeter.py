import random


def test(gcd, n_iter=100):
    for i in range(n_iter):
        c = random.randint(0, 1024)
        a = c * random.randint(0, 128)
        b = c * random.randint(0, 128)
        assert gcd(a, a) == gcd(a, 0) == a
        assert gcd(b, b) == gcd(b, 0) == b
        d = gcd(a, b)
        assert a % d == b


# naive version of algorithm for searching greatest common delimeter
def gcd(a, b):
    assert a >= 0 and b >= 0
    for d in reversed(range(max(a, b) + 1)):
        if d == 0 or a % d == b % d == 0:
            return d


# print(gcd(8, 3))
# print(gcd(8, 0))
# print(gcd(0, 0))


def gcd2(a, b):
    while a and b:
        if a >= b:
            a %=b
        else:
            b %= a
    return max(a, b)


# print(gcd2(87946131, 78941613))
# print(gcd2(87946131, 78941611))


def gcd3(a,b):
    assert a >= 0 or b >= 0
    if a ==0 or b ==0:
        return max(a,b)
    elif a >= b:
        return gcd3(a % b, b)
    else:
        return gcd3(a, b % a)


def gcd4(a, b):
    assert a >= 0 or b >= 0
    if a == 0 or b ==0:
        return max(a, b)
    return gcd4(b % a, a)


print(gcd4(15, 6))