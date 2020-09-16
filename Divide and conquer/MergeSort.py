"""
Алгоритм сортировки слиянием
"""


def Merge(A, B, counter):
    i = j = k = 0
    C = [0] * (len(A) + len(B))
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
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

    return C, counter


def MergeSort(array):
    if len(array) < 2:
        return array
    else:
        mid = len(array) // 2
        A = array[:mid]
        B = array[mid:]
        A = MergeSort(A)
        B = MergeSort(B)

    return Merge(A, B)
