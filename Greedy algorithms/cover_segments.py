import string
import sys

#input = open('1.txt', 'r') //расскомментировать решая задачу локально
input = sys.stdin
S = []
n = int(input.readline())
for i in range(1,n+1):
  x,y = map(int, input.readline().split())
  S.append([x,y])


def getKey(item):
    return item[1]
S.sort(key = getKey)

solution = []
i = 0
while i<len(S):
    temp = S[i][1]
    solution.append(temp)
    i+=1
    while i<len(S) and S[i][0] <= temp:
        i+=1

print(len(solution))
for elem in solution:
    print(elem,end=' ')
