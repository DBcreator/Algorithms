def binary_search(A,B,n):
    indexes = []
    for k in range(len(B)):
        l = 0
        r = n - 1
        while l<= r:
            m = int(l + (r-l)/2)
            if B[k] == A[m]:
                indexes.append(m+1)
                break
            elif B[k] < A[m]:
                r = m-1
            elif B[k] > A[m]:
                l = m+1
        if k > len(indexes)-1:
            indexes.append(-1)
    return indexes

def main():
    n, *A = map(int, input().split())
    k, *B = map(int, input().split())
    answer = binary_search(A,B,n,k)
    for elem in answer:
        print(elem,end=' ')


if __name__ == '__main__':
    main()