# 터렛
def findPoint(dist,r1,r2):
    if dist == 0 and r1 == r2:
        return -1
    if dist == (r1+r2) :    # 외접
        return 1
    if dist == abs(r1-r2) : # 내접
        return 1
    if (r1+r2) > dist > abs(r1-r2) :    # 두점에서 만남
        return 2
    else :
        return 0
    
for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int,input().split(' '))
    dist = ((x1-x2)**2 + (y1-y2)**2)**0.5
    print(findPoint(dist,r1,r2))