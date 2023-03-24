# 히스토그램에서 가장 큰 직사각형
import sys
input = sys.stdin.readline

def histogram(N, read):
    stack = []
    finish = 0 # 인덱스들의 차(가로) * 값(세로)

    for i in range(N):
        value = read[i]
        start = i
        while stack and stack[-1][1] > value:
            start, preValue = stack.pop()
            finish = max(finish,(i-start)*preValue)
        stack.append([start,value])

    while stack :
        start, preValue = stack.pop()
        finish = max(finish,(N-start)*preValue)

    print(finish)

while True :
    read = list(map(int,input().split(' ')))
    N = read[0]
    if N == 0 :
        break
    histogram(N, read[1:])