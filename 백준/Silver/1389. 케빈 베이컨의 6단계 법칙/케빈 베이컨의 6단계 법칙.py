from collections import deque

def bfs(x):
    q.append(x)
    visited = [-1 for _ in range(N)]
    visited[x] = 0
    
    while q:
        x = q.popleft()
        for i in rel[x]:
            if visited[i] == -1:
                visited[i] = visited[x] + 1
                q.append(i)
    cnt = 0
    for i in range(N):
        if visited[i] != -1:
            cnt += visited[i]
    return cnt

N, M = map(int, input().split())
rel = [[] for _ in range(N)]
q, arr, ans = deque(), [], []

for _ in range(M):
    x, y = map(int, input().split())
    rel[x-1].append(y-1)
    rel[y-1].append(x-1)

for i in range(N):
    arr.append(bfs(i))

for i in range(N):
    if arr[i] == min(arr):
        ans.append(i)
        
print(min(ans)+1)
