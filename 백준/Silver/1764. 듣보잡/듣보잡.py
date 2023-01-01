nohear,nosee = map(int,input().split())

noheararray = set()
ansarray = set()
ans = 0

for _ in range(nohear):
    noheararray.add(input())

for _ in range(nosee):
    temp = input()
    if temp in noheararray:
        ansarray.add(temp)
        ans += 1

print(ans)
for i in sorted(ansarray) :
    print(i)
