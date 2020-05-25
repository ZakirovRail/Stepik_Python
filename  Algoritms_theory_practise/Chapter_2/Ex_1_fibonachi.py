# Дано целое число 1≤n≤40, необходимо вычислить n-е число Фибоначчи


def fib(n):
    f0, f1 = 0, 1
    for i in range(n-1):
        f0, f1 = f1, f0+f1
    return f1


def main():
    n = int(input())
    print(fib(n))


if __name__ == '__main__':
    main()