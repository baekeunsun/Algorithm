# 공 넣기
N,M = map(int,input().split(' '))
answer = [0]*N

for _ in range(M):
    start, end, value = map(int,input().split(' '))
    for i in range(start-1, end):
        answer[i] = value

print(*answer)