# 암호 만들기
# 암호 조건 : a,e,i,o,u 중 최소 두개 /  알파벳 오름차순
import itertools

L, C = map(int,input().split())
string = list(map(str,input().split()))

ja = []
mo = []

for i in string :
    if i in ['a','e','i','o','u'] :
        ja.append(i)
    else :
        mo.append(i)

answer = []
tmp = []
for n in range(1,min(len(ja)+1, L-1)):
    for case1 in (itertools.combinations(ja, n)) :
        for case2 in (itertools.combinations(mo, L - n)):
            tmp = list(case1 + case2)
            tmp.sort()
            answer.append(tmp)
answer.sort()

for i in answer :
    print(*i, sep='')
    
    
