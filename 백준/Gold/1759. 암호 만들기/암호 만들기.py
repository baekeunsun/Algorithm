# 암호 만들기
# 암호 조건 : a,e,i,o,u 중 최소 두개 /  알파벳 오름차순
from itertools import combinations
import sys 
input=sys.stdin.readline

L, C = map(int,input().split())
string = sorted(input().split())
words = combinations(string, L)

for word in words :
    count = 0
    for w in word :
        if w in 'aeiou' :
            count += 1
    if count >= 1 and (L-count) >= 2 :
        print(''.join(word))
