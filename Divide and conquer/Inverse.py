def Inverse(C):
    if len(C) == 1:
        return C, 0

    else:
        mid = len(C) // 2
        A = C[:mid]
        B = C[mid:]
        A, c1 = Inverse(A)
        B, c2 = Inverse(B)
        i = j = k = 0
        counter = 0 + c1 + c2
        while i < len(A) and j < len(B):
            if A[i] <= B[j]:
                C[k] = A[i]
                i += 1
                k += 1
            else:
                C[k] = B[j]
                j += 1
                k += 1
                counter += len(A) - i

        while i < len(A):
            C[k] = A[i]
            i += 1
            k += 1

        while j < len(B):
            C[k] = B[j]
            j += 1
            k += 1
            counter += len(A) - i

        return C,counter


def main():
    n = int(input())
    C = list(map(int, input().split()))
    print(Inverse(C)[1])

if __name__ == '__main__':
    main()

