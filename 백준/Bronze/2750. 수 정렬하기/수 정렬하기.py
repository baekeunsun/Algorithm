# 수 정렬하기
N = int(input())
number = list(int(input()) for _ in range(N))
number.sort()

for i in range(N):
    print(number[i])