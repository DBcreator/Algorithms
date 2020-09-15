def stairs(n,numbers):
    D = [0] * n
    D[0] = numbers[0]
    for i in range(1,n):
        D[i] = max(D[i-1]+numbers[i],D[i-2]+numbers[i])

    return D[n-1]


def main():
    n = int(input())
    numbers = list(map(int, input().split()))

    print(stairs(n,numbers))

if __name__ == '__main__':
    main()