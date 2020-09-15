from math import inf

def calculator(n):
    D = [inf] * n
    D[0] = 0
    prev = [0] * n

    for i in range(1, n+1):
        for k in (i*2, i*3, i+1):
            if k-1 < n and D[i-1] + 1 < D[k-1]:
                D[k-1] = D[i-1] + 1
                prev[k-1] = i

    return D[-1], prev


def main():
    n = int(input())
    k, sub = calculator(n)
    ans = [n,]
    while n > 1:
        ans.append(sub[n-1])
        n = sub[n-1]
    ans = ans[::-1]
    print(k)
    for elem in ans:
        print(elem, end=' ')

if __name__ == '__main__':
    main()
