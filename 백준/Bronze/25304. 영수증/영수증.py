X = int(input())
N = int(input())
stuff = 0

for _ in range(N):
    a,b = map(int,input().split())
    stuff += a*b

if stuff == X:
    print("Yes")
else:
    print("No")
