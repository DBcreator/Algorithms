# Найти остаток от деления n числа Фибоначчи на m
# Используется период Пизано
# Пока не проходит 5 тест

def fib_mod(n, m):
    Fib = [0] * (n+1)
    Fib[1] = 1
    T_Pisano = [0, 1]
    T = 0
    for i in range(2, n+1):
        Fib[i] = (Fib[i-1] + Fib[i-2]) % m
        T_Pisano.append(Fib[i])
        if len(T_Pisano) > 2:
            if T_Pisano[-2] == 0 and T_Pisano[-1] == 1:
                T = len(T_Pisano) - 2
    if T != 0:
        index = n % T
        answer = T_Pisano[index]
    else:
        answer = n%m
    return answer

def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()