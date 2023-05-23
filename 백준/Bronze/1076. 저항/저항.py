# 저항
value = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
answer = 0
for i in range(1,-1,-1):
    answer += value.index(input())*(10**i)

print(answer* (10**value.index(input())))
