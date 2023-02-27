dp = [0 for _ in range(1000001)]
dp[2] = 1
dp[3] = 1
N = int(input())

if N > 3 :
    for n in range(4, N+1):
        dp[n] = min(n,dp[n-1]+1)
        if n % 3 == 0:
            dp[n] = min(dp[n],dp[n//3]+1)
        if n % 2 == 0:
            dp[n] = min(dp[n], dp[n//2]+1)
            
print(dp[N])