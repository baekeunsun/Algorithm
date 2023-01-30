def solution(n):
    answer = []
    while n :
        i = 1
        answer.append(n %(10**i))
        n = n//(10**i)
        i += 1
        
    return answer