N = int(input())
i = 0

while N > 0:
    if i % 1000 == 666:
        for j in range(1000):
            N -= 1
            if N == 0:
                print(i * 1000 + j)
                break
    elif i % 100 == 66:
        for j in range(100):
            N -= 1
            if N == 0:
                print(i * 1000 + 600 + j)
                break
    elif i % 10 == 6:
        for j in range(10):
            N -= 1
            if N == 0:
                print(i * 1000 + 660 + j)
                break
    else:
        N -= 1
        if N == 0:
            print(i * 1000 + 666)
            break
    i += 1