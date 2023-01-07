import sys
from collections import deque

input = sys.stdin.readline

def check(x,y,z):
    if [x,y,z] not in array :
        array.append([x,y,z])
        queue.append([x,y,z])

def bfs () :
    while queue:
        a,b,c = queue.popleft()
        
        # A -> B
        temp = min(a,B-b)
        check(a-temp,b+temp,c)
        # A - > C
        temp = min(a,C-c)
        check(a-temp,b,c+temp)
        # B -> A
        temp = min(b,A-a)
        check(a+temp,b-temp,c)
        # B -> C
        temp = min(b,C-c)
        check(a,b-temp,c+temp)
        # C -> A
        temp = min(c,A-a)
        check(a+temp,b,c-temp)
        # C -> B
        temp = min(c,B-b)
        check(a,b+temp,c-temp)

A,B,C = map(int, input().split())
array =[[0,0,C]]
queue = deque([[0,0,C]])

bfs()

ans = []

for i,j,k in array :
    if i == 0:
        ans.append(k)

ans.sort()
for i in ans:
    print(i, end=" ")
