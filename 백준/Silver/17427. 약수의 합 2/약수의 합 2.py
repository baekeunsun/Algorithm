# 약수의 합2
import sys
input = sys.stdin.readline

N = int(input())
answer = 0
for number in range(1,N+1):
    answer += (number)*(N//number)

print(answer)