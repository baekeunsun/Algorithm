def check(W,H,X,Y,a,b) :
    # 직사각형
    if X <= a <= X+W and Y <= b <= Y+H :
        return 1
    # 왼쪽 반원
    elif (a-X)**2 + (b-(Y+H/2))**2 <= (H/2)**2 :
        return 1
    elif (a-X-W)**2 + (b-(Y+H/2))**2 <= (H/2)**2 :
        return 1
    else :
        return 0

W,H,X,Y,P = map(int, input().split())
result = 0

for _ in range(P) :
    a, b = map(int,input().split())
    result += check(W,H,X,Y,a,b)

print(result)


