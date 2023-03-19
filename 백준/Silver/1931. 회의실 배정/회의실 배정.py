# 회의실 배정
import sys
input = sys.stdin.readline

N = int(input())
time = []
answer = 0

for _ in range(N):
    time.append(list(map(int,input().split(' '))))

time.sort(key=lambda x : (x[1],x[0]))

tmp = 0
for i in range(N):
    if tmp <= time[i][0]:
        answer += 1
        tmp = time[i][1]

print(answer)