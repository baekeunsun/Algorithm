# 인공지능 시게
time = list(map(int,input().split(' ')))
time[2] += int(input())
maxTime = [24,60,60]

for i in range(2,-1,-1):
    if time[i] >= maxTime[i] :
        tmp = time[i]
        time[i] = tmp%maxTime[i]
        if i != 0 :
            time[i-1] += tmp//60

print(*time)