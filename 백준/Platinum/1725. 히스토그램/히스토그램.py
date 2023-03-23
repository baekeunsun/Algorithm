# 히스토그램 
import sys
input = sys.stdin.readline

N = int(input())
stack = []  # 인덱스, 값
finish = 0 # 인덱스들의 차(가로) * 값(세로)

for i in range(N):
    value = int(input())
    start = i
    while stack and stack[-1][1] >= value:
        start, preValue = stack.pop()
        finish = max(finish,(i-start)*preValue)
    stack.append([start,value])

while stack :
    start, preValue = stack.pop()
    finish = max(finish,(N-start)*preValue)

print(finish)