import sys
from _collections import deque
r,c=map(int,input().split())
maps=[list(p for p in sys.stdin.readline().strip()) for _ in range(r)]
visit=[[0]*c for _ in range(r)]
dr=[1,0,-1,0]
dc=[0,-1,0,1]
queue=deque()

for i in range(r):
    for j in range(c):
        if maps[i][j]=='*':
            queue.append([i,j])
        elif maps[i][j]=='S':
            queue.appendleft([i,j])
        elif maps[i][j]=='D':
            target_r=i
            target_c=j
flag=False

while queue:
    
    if flag:
        break
    pr, pc = queue.popleft()
    for i in range(4):
        nr,nc=pr+dr[i],pc+dc[i]
        if nr<0 or nr>=r or nc<0 or nc>=c:
            continue

        
        if maps[pr][pc]=='*':
            if maps[nr][nc]=='.' or maps[nr][nc]=='S':
                maps[nr][nc]='*'
                queue.append([nr,nc])
       
        elif maps[pr][pc] == 'S':
            if maps[nr][nc] == '.':
                maps[nr][nc] = 'S'
                visit[nr][nc] = visit[pr][pc] + 1
                queue.append([nr,nc])
            
            elif maps[nr][nc] == 'D':
                flag=True
                visit[nr][nc]=visit[pr][pc]+1
                break


if visit[target_r][target_c]==0:
    print('KAKTUS')
else: print(visit[target_r][target_c])