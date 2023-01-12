array = [list(map(int,input().split())) for _ in range(5)]
ans = set()
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def dfs(num,x,y,temp):
    if num >= 5 :
        ans.add(temp)
        return
    for i in range(4):
        ix = x + dx[i]
        iy = y + dy[i]
        if 0 <= ix < 5 and 0<= iy < 5:
            dfs(num+1,ix,iy,temp*10 + array[ix][iy])

            
for i in range(5):
    for j in range(5):
        dfs(0,i,j,array[i][j])

print(len(ans))
        

