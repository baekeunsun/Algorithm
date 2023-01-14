from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):   # T동안 반복
    N, K = map(int,input().split()) # 건물의 개수와 건물간 규칙개수
    buildTime = [0] + list(map(int,input().split()))
    relation = [[] for _ in range(N+1)]
    parentsNum = [-1] + [0]*(N)
    
    for _ in range(K):
        X, Y = map(int,input().split()) # X를 거쳐야 Y가 됨
        relation[X].append(Y) 
        parentsNum[Y] += 1
        
    W = int(input())
    dp = [0]*(N+1)
    q = deque()
    
    for i in range(1,N+1):  # 진입차수가 0인 정점 찾기
        if parentsNum[i] == 0:  # 여러개일수 있으니까 break안함
            q.append(i)
            dp[i] = buildTime[i]
            
    while q :# DP 메모이제이션
        node = q.popleft()
        for nextNode in relation[node]:
            parentsNum[nextNode] -= 1
            dp[nextNode] = max(dp[nextNode], dp[node]+buildTime[nextNode])
            if parentsNum[nextNode] == 0:
                q.append(nextNode)
        if parentsNum[W] == 0:
            print(dp[W])
            break