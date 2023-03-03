import sys
input = sys.stdin.readline
sys.setrecursionlimit(300000)

n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
array = list([0 for _ in range(n)]for _ in range(n))

def dfs(x,y):
    if array[x][y] != 0 :
        return array[x][y]
    array[x][y] = 1
    for i in range(4):
        ix = x + dx[i]
        iy = y + dy[i]

        if 0 <= ix < n and 0 <= iy < n and forest[ix][iy] > forest[x][y]:
            array[x][y] = max(array[x][y],dfs(ix,iy)+1)

    return array[x][y]

ans = 0
for i in range(n):
    for j in range(n):
            ans = max(ans,dfs(i,j))
print(ans)
