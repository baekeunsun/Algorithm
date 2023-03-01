import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    tmp = list(input().split())
    print(f"Case #{i+1}:",end=" ")
    while tmp :
        print(tmp.pop(),end=" ")
    print()
