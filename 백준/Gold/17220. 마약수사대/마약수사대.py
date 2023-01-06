from collections import deque

N,M = map(int,input().split())
dic = {}
root = set(chr(i+ord('A')) for i in range(N))
ans = set()
num = 0
for _ in range(M):
    x,y = map(str,input().split())
    if x in dic:
        dic[x].append(y)
    else :
        dic[x] = [y]
        
for i in dic.values():
    for j in i:
        ans.add(j)
        
root = list(root-ans)
for i in input().split()[1:]:
    if i in dic: # A일때
        del dic[i]
    for j in dic.keys():
        if i in dic[j]:
            dic[j].remove(i)

count =0
visited = [0 for i in range(N)]
while root:
    tmp = root.pop()
    if tmp in dic:
        for i in dic[tmp]:
            tmp_n = ord(i)-ord('A')
            if not visited[tmp_n]:
                count+=1
                visited[tmp_n] = 1
                root.append(i)
print(count)
