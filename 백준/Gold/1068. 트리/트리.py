# 트리
def dfs(v):
    tree[v] = -2
    for i in range(N):
        if v == tree[i]:
            dfs(i)
            
N = int(input())
tree = list(map(int, input().split()))
E = int(input())

dfs(E)
answer = 0

for i in range(N):
    if tree[i] != -2 and i not in tree:
        answer += 1

print(answer)
