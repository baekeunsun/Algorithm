# 귀찮음
n = int(input())
a = list(map(int,input().split(' ')))
a.sort()
A = sum(a)
answer = 0
for i in a :
    answer += i * (A-i)
    A -= i

print(answer)
