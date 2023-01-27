import heapq

N = int(input())
cards = []
for i in range(N):
    cards.append(int(input()))

cards.sort(reverse=True)
heapq.heapify(cards)
answer = 0
while len(cards) != 1 :
    tmp = heapq.heappop(cards) + heapq.heappop(cards)
    heapq.heappush(cards,tmp)
    answer += tmp
print(answer)