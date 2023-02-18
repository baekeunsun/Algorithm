from itertools import combinations

N, M = map(int,input().split())

array = [list(map(int,input().split())) for _ in range(N)]
chicken = []
house = []
ans = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 치킨 집 찾아내기 chicken에 저장
for i in range(N):
    for j in range(N):
        if array[i][j] == 2 :
            chicken.append((i,j))
        elif array[i][j] == 1:
            house.append((i,j))

for chi in list(combinations(chicken,M)):
    finalcount = 0
    for h in house:
        count = 700
        for c in chi:
            count = min(count, abs(c[0] - h[0]) + abs(c[1] - h[1]))
        finalcount += count
    ans.append(finalcount)
    
        
print(min(ans))
        
