N, K = map(int,input().split())
load = [[0,0]] + [list(map(int,input().split())) for _ in range(N)]
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1):
    weight = load[i][0]
    value = load[i][1]
    
    for nowWeight in range(1,K+1) :
        if nowWeight < weight :
            dp[i][nowWeight] = max(dp[i-1][nowWeight], dp[i][nowWeight-1])
        else :
            dp[i][nowWeight] = max(value + dp[i-1][nowWeight-weight], dp[i-1][nowWeight])

print(dp[N][K])
