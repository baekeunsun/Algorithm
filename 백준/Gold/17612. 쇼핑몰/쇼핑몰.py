# 17612 : 쇼핑몰
import heapq
import sys
input = sys.stdin.readline

N,k = map(int,input().split(' '))   # N: 고객수 k: 계산대 수
answer = 0
cashier = []   # 물품번호(N값 뺀거), 계산대 번호, 고객번호
finish = []

for i in range(N):
    customer, things = map(int,input().split(' '))
    if len(cashier) < k :  # 카트 꽉 안참 -> 처음
        heapq.heappush(cashier,[things,(i+1),customer])
    else :  # 카트 꽉 참 -> 빼고 넣기
        time, nowCashier, outCustomer = heapq.heappop(cashier)
        heapq.heappush(cashier,[things+time,nowCashier, customer])
        heapq.heappush(finish,[time, -nowCashier, outCustomer])

while cashier :
    time, nowCashier, outCustomer = heapq.heappop(cashier)
    heapq.heappush(finish,[time, -nowCashier, outCustomer])

for j in range(N):
    tmp = heapq.heappop(finish)
    answer += tmp[2] * (j+1)

print(answer)