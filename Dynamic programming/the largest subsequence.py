def subseq(array,n):
    D = [0]*n
    prev = [-1]*n

    for i in range(n):
        D[i] = 1
        prev[i] = -1
        for j in range(i):
            if array[i] % array[j] == 0 and D[j] + 1 > D[i]:
                D[i] = D[j] + 1
                prev[i] = j
    return max(D)


def main():
    n = int(input())
    array = list(map(int, input().split()))
    print(subseq(array,n))

if __name__ == '__main__':
    main()