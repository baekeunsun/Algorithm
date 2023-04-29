# 영식이와 친구들
N, M, L = map(int,input().split())
ball = list(0 for _ in range(N))
i = 0
answer = -1

while True :
    ball[i] += 1
    answer += 1
    if max(ball) >= M :
        break
    if ball[i] % 2 == 0 :
        i = (i - L) % N
    else :
        i = (i + L) % N

print(answer)
