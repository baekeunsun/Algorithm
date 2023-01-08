n, k = map(int,input().split())

st = [[0,0]]
snap = [[0]*(k+1) for _ in range(n+1)]

for _ in range(n):
    st.append(list(map(int,input().split())))

for i in range(1,n+1):
    for j in range(1,k+1):
        weight = st[i][0]
        value = st[i][1]
        
        if j < weight:
            snap[i][j] = max(snap[i-1][j], snap[i][j-1])
            
        else:
            snap[i][j] = max(value + snap[i-1][j-weight] , snap[i-1][j])

print(snap[n][k])