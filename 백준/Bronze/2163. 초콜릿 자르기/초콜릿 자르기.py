# 초콜릿 자르기
N,M = map(int,input().split(' '))
answer = 0
if N > 1 :
    answer += (N-1)
if M > 1 :
    answer += N*(M-1)

print(answer)