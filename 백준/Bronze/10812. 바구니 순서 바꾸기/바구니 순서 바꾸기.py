# 바구니 순서 바꾸기
N,M = map(int,input().split(' '))
basket = [0] + list(i for i in range(1,N+1))

for _ in range(M):
    begin, end, mid = map(int,input().split(' '))
    beginBasket = basket[begin:mid]
    midBasket = basket[mid:end+1]
    basket = basket[:begin] + midBasket + beginBasket + basket[end+1:]

print(*basket[1:])

