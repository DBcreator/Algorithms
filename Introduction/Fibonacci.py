# Найти n-ое число Фибоначч

def fib(n):
    Fib = [0]*(n+1)
    Fib[1] = 1
    for i in range(2,n+1):
        Fib[i] = Fib[i-1] + Fib[i-2]
    return Fib[n]


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()