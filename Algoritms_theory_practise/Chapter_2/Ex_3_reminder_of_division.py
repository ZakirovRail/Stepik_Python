def fib(n, m):
    fibs = list()
    fibs.append(1 % m)
    fibs.append(1 % m)
    for i in range(n - 2):
        curr = (fibs[-1] + fibs[-2]) % m
        if curr == 1 and fibs[-1] == 1:
            period = i - 1

            i = len(fibs[:-1])
            return fibs[:-1][(n) % i - 1]
        fibs.append(curr)

    return fibs[-1]


def main():
    n = int(input())
    m = int(input())
    print(fib(n, m))


if __name__ == '__main__':
    main()













