def various(n):
    numbers = []
    for i in range(1,n):
        n -= i
        numbers.append(i)
        if n >= i+1:
            continue
        else:
            numbers.pop()
            numbers.append(n+i)
            break
    return numbers

def main():
    n = int(input())
    if n == 1:
        print(1)
        print(1)
    else:
        answer = various(n)
        print(len(answer))
        for i in answer:
            print(i, end = ' ')

if __name__ == '__main__':
    main()