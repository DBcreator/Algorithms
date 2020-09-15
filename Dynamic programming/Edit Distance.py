import math

inf = math.inf


def diff(a, b):
    return 0 if a == b else 1


def edit_distance(i, j, str1, str2, D):
    if D[i][j] == inf:
        if i == 0:
            D[i][j] = j
        elif j == 0:
            D[i][j] = i
        else:
            ins = edit_distance(i, j - 1, str1, str2, D) + 1
            delete = edit_distance(i - 1, j, str1, str2, D) + 1
            sub = edit_distance(i - 1, j - 1, str1, str2, D) + diff(str1[i - 1], str2[j - 1])
            D[i][j] = min(ins, delete, sub)

    return D[i][j]


str1 = str(input())
str2 = str(input())

D = [[inf] * (len(str2) + 1) for i in range(len(str1) + 1)]
i = len(str1)
j = len(str2)
ans = edit_distance(i=i, j=j, str1=str1, str2=str2, D=D)

print(ans)
