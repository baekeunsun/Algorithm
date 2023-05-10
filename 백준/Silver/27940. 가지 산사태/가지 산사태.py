# 가지 산사태
import sys
input = sys.stdin.readline

N, M, K = map(int,input().split())   # 농장층수, 비 횟수, 버틸수있는 빗물 양

total = 0
for i in range(1,M+1):
    t, r = map(int,input().split())  # 1층~t층, r만큼 비
    total += r
    if total > K :
        print(i,1)
        sys.exit()
    
print(-1)
