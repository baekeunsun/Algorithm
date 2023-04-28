# 핸드폰 요금
N = int(input())
use = list(map(int,input().split()))

M = 0
Y = 0

def ys(time):
    if time < 30 :
        return 10
    else :
        return (time // 30)*10 + 10

def ms(time):
    if time < 60 :
        return 15
    else :
        return (time // 60)*15 + 15
    

for u in use :
    M += ms(u)
    Y += ys(u)

if M < Y :
    print("M", M)
elif Y < M :
    print("Y", Y)
else :
    print("Y M", M)
        
