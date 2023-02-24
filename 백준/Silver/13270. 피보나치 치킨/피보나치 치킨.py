n = int(input())
dp = [[0]*(2) for _ in range(100000)]
a = 1
i = 2

for k in range(1,n+1):
    dp[k][0] = 100000000

while i <= n:
    for j in range(i, n+1):
        dp[j][0] = min(dp[j][0], dp[j-i][0] + a)
        dp[j][1] = max(dp[j][1], dp[j-i][1] + a)

    i,a = i+a, i

print(dp[n][0], dp[n][1])
