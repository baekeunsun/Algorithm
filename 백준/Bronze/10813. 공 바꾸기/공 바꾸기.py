# 공 바꾸기
N, M = map(int,input().split(' '))
basket = [0] + list(i for i in range(1,N+1))

for _ in range(M):
    a,b = map(int,input().split(' '))
    tmp = basket[a]
    basket[a] = basket[b]
    basket[b] = tmp

print(*basket[1:])