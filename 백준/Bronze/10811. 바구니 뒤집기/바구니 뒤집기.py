# 바구니 뒤집기
N, M = map(int,input().split(' '))
basket = list(i for i in range(N+1))
for _ in range(M):
    a,b = map(int,input().split(' '))
    basket[a:b+1] = basket[b:a-1:-1]
print(*basket[1:])
