# 나누기
import sys

N = (int(input())//100)*100
F = int(input())

remainder = N % F
if remainder > 0:
    answer = (N+(F-remainder)) % 100
else :
    answer = 0

print('{0:02d}'.format(answer))
