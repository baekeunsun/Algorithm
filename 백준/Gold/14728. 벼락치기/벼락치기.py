N,T = map(int,input().split())
dp =[0]*(T+1)

for _ in range(N):
    time, score = map(int,input().split())

    for nowTime in range(T,time-1,-1) :
        dp[nowTime] = max(dp[nowTime], dp[nowTime-time]+score)

print(dp[T])
