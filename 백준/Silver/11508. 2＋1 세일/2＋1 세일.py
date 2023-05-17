# 2+1 세일
N = int(input())
buy = list(int(input()) for _ in range(N))
buy.sort()
answer = 0

for i in range(N//3):
    answer += buy.pop()
    answer += buy.pop()
    buy.pop()
    
while buy :
    answer += buy.pop()

print(answer)
