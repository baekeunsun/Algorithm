from collections import defaultdict

T = int(input())

for _ in range(T):
    C = int(input())
    dic = defaultdict(int)
    ans = 1
    
    for _ in range(C):
        v,k = map(str,input().split())
        dic[k] += 1

    if len(dic.keys()) == 1 :
        for i in dic.keys() :
            print(dic.get(i))
        
    else :
        for i in dic.keys() :
            ans *= (dic.get(i)+1)
            
        print(ans-1)
