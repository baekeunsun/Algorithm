from collections import deque

def distance(sx, sy, fx, fy):
    return (abs(sx-fx) + abs(sy-fy))

def bfs(home, festival):
    visited = set()
    queue = deque([home])
    
    while queue :
        x,y = queue.popleft()

        if distance(x, y, festival[0], festival[1]) <= 1000 :   # 페스티벌 도착
            return ("happy")
        
        for i in range(marketCount):
            ix, iy = market[i]
            if (ix, iy) not in visited :   # 방문안함
                if distance(x,y,ix,iy) <= 1000 :    # 갈 수 있는 편의점
                    visited.add((ix,iy))
                    queue.append([ix,iy])
    return ("sad")

for _ in range(int(input())) :  # 테스트케이스 t
    marketCount = int(input())
    home = list(map(int,input().split(' ')))
    market = list()
    for _ in range(marketCount):
        market.append(list(map(int,input().split(' '))))
    festival = list(map(int,input().split(' ')))
        
    print(bfs(home, festival))
