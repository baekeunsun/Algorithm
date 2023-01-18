from sys import stdin

N = int(stdin.readline())
A = [int(stdin.readline()) for _ in range(N)]
dp = [1 for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))