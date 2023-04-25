# 평균은 넘겠지
T = int(input())
for _ in range(T):
    N = list(map(int,input().split(' ')))
    avg = sum(N[1:]) / N[0]
    student = 0
    for i in N[1:]:
        if i > avg :
            student += 1
    print('%.3f' %(student/N[0]*100) +"%")