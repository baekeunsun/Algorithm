ans = [ x for x in range(1,10001)]
i = 1

while i < 10000 :
    tmp = i + sum(map(int,str(i)))
    if tmp in ans :
        ans.remove(tmp)
    i+=1
  
print(*ans,sep='\n')
