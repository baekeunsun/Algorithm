import itertools

N,M = map(int,input().split(' '))
Nlist = [ i for i in range(1,N+1)]

perm = itertools.permutations(Nlist,M)

for p in perm:
    print(*p)