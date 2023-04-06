# 전화번호 목록
import sys
input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    number = []
    N = int(input().rstrip())
    
    for _ in range(N):
        number.append(input().rstrip())
    number.sort()
    answer = "YES"

    for n in range(len(number) - 1):
        if number[n] == number[n+1][:len(number[n])] :
            answer = "NO"
            break

    print(answer)