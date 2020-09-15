def knapsack(n, W, C_w):
    summary = 0
    for item in C_w:
        if item[1] < W and W > 0:
            W = W - item[1]
            summary += item[0]

        elif item[1] >= W and W > 0:
            summary += (item[0] / item[1]) * W
            W = 0

    return '{:.3f}'.format(summary)


def read():
    n, W = map(int, input().split())
    C_w = []
    for i in range(n):
        c, w = map(int, input().split())
        C_w.append([c, w])
    C_w.sort(key=lambda item: item[0] / item[1], reverse=True)
    return n, W, C_w


def main():
    n, W, C_w = read()
    print(knapsack(n, W, C_w))


if __name__ == '__main__':
    main()
