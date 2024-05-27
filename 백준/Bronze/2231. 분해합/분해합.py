def result(N):
    for i in range(1, N + 1):
        digit_sum = sum(map(int, str(i)))
        if i + digit_sum == N:
            return i
    return 0

N = int(input())
print(result(N))