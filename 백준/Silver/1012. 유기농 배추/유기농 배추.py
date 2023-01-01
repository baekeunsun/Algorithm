T = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x,y):
    queue = [[x,y]]
    while queue:
        a,b = queue[0][0],queue[0][1]
        del queue[0]
        for r in range(4):
            i = a + dx[r]
            j = b + dy[r]
            if 0 <= i < N and 0 <= j < M and bae[i][j] == 1:
                bae[i][j] = 0
                queue.append([i,j])

for i in range(T):
    M,N,K = map(int,input().split())
    bae = [[0]*M for i in range(N)]
    count = 0
    
    for k in range(K):
        a,b = map(int, input().split())
        bae[b][a] = 1
        
    for x in range(N):
        for y in range(M):
            if bae[x][y] == 1:
                bfs(x, y)
                bae[x][y] = 0
                count += 1
                    
    print(count)


        
        
