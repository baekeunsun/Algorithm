from collections import deque

def solution(n, computers):    
    ans = 0
    check = [0]*n
    q = deque()
    
    for i in range(n):
        if check[i] == 0 :  # 아직 안갔음
            q.append(i)
            while q :
                tmp = q.popleft()
                check[tmp] = 1
                for j in range(n):
                    if (computers[tmp][j] == 1) and (check[j] == 0):
                        q.append(j)
            ans += 1
            
    
    return ans