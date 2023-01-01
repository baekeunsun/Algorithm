user = list(map(int,input().split()))
white = [1,1,2,2,2,8]
answer = []

for i in range(6):
    answer.append(white[i]-user[i])

print(*answer)
    
