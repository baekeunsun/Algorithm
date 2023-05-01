# 피리부는 사나이
N, M = map(int,input().split())
Map = list(list(map(str,input())) for _ in range(N))

group = [[-1 for _ in range(M)] for _ in range(N)]

direction = ['L','R','U','D']
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def move(x,y,idx):
    global answer
    if group[x][y] != -1:   # 방문함
        if group[x][y] == idx:
            answer += 1
        return  # 만일 형성된 사이클에 방문하더라도 idx가 다르기때문에 괜찮다

    group[x][y] = idx
    i = direction.index(Map[x][y])
    move(x + dx[i], y + dy[i], idx)

idx = 0
answer = 0
for n in range(N):
    for m in range(M):
        move(n,m,idx)
        idx += 1


print(answer)
