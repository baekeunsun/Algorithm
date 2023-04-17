# 가지 교배
n = int(input())    # 가지 품종 수
eggplant = [0] + list(map(str,input().split(' ')))
m, k = map(int,input().split(' '))
flags = []

for _ in range(m):
    assist = list(map(int,input().split(' ')))
    flag = True
    for have in assist:
        if eggplant[have] == "P":
            flag = False
            break
    flags.append(flag)
    
if True in flags :
    print("W")
else :
    print("P")
