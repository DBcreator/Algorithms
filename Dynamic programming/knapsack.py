def knapsack(W, n, weights):
    D = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if w >= weights[i - 1]:
                D[i][w] = max(D[i - 1][w], D[i - 1][w - weights[i - 1]] + weights[i - 1])
            else:
                D[i][w] = D[i - 1][w]
    return D[n][W]


def main():
    W, n = map(int, input().split())
    weights = list(map(int, input().split()))

    print(knapsack(W, n, weights))


if __name__ == '__main__':
    main()
