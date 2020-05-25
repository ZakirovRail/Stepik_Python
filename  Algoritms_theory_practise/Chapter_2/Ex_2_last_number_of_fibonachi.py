# Дано число 1≤n≤10(7), необходимо найти последнюю цифру nn-го числа Фибоначчи.


def fib(n):
    f0, f1 = 0, 1
    for _ in range(n-1):
        f0, f1 = f1, (f0+f1) % 10
    return f1


def main():
    n = int(input())
    print(fib(n))


if __name__ == '__main__':
    main()