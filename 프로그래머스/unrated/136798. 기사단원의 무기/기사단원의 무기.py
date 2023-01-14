def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        count = 0
        if i == 1:
            count = 1
        else:
            for j in range(1,int(i**(1/2))+1):
                if i%j == 0 :
                    if j == i//j:
                        count += 1
                    else :
                        count += 2
                if count > limit :
                    count = power
                    break
        answer += count
    return answer