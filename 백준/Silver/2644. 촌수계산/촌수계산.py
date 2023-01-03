from collections import deque

n = int(input())
t1, t2 = map(int, input().split())
m = int(input())
r = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    r[x].append(y)
    r[y].append(x)

count = 0
q = deque([[t1, count]])
while q :
    value = q.popleft()
    t1 = value[0]
    count = value[1]
    if t1 == t2:
        print(count)
        exit()
    
    if not visited[t1]:
        count += 1
        visited[t1] = True
        for e in r[t1]:
            if not visited[e]:
                q.append([e,count])
print(-1)