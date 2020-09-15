def freq(s):
    f = []
    for symbol in s:
        if symbol not in f:
            k = 0
            for i in range(len(s)):
                if symbol == s[i]:
                    k+=1
            f.append([symbol, k])
    return f

def Extract2min(array):
    if array[0][1] < array[1][1]:
        min1 = 0
        min2 = 1
    else:
        min1 = 1
        min2 = 0

    for i in range(2, len(array)):
        if array[i][1] < array[min1][1]:
            temp = min1
            min1 = i
            if array[temp][1] < array[min2][1]:
                min2 = temp
        elif array[i][1] < array[min2][1]:
            min2 = i

    return array[min1],array[min2]


def Huffman(s):
    H = freq(s)
    for i in range(len(H)):
        min1, min2 = Extract2min(H)



def main():
    s = str(input())
    print(Huffman(s))

def test():
    s = str(input())
    print(freq(s))


if __name__ == '__main__':
    pass
