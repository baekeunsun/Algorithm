import sys
sys.setrecursionlimit(50000)
R,C = map(int,input().split())

array = [list(map(str,input())) for i in range(R)]
flag = list([False for i in range(C)] for i in range(R))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

v_temp = 0
o_temp = 0

v_num = 0
o_num = 0

def find(x,y):
    global v_temp
    global o_temp
    if array[x][y] == '#':
        return
    else:
        if array[x][y] == 'v':
            v_temp += 1
        elif array[x][y] == 'o':
            o_temp += 1
        flag[x][y] = True
            
        for i in range(4):
            ix = x + dx[i]
            iy = y + dy[i]
            
            if 0 <= ix < R and 0 <= iy < C and flag[ix][iy] == False:
                
                find(ix,iy)


for x in range(R):
    for y in range(C):
        if flag[x][y] == False:
            v_temp = 0
            o_temp = 0
            find(x,y)
            if o_temp > v_temp :
                o_num += o_temp
            else :
                v_num += v_temp

print(o_num, v_num)
