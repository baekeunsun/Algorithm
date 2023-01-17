def solution(s):
    answer = []
    criteria = dict()
    
    for i in range(len(s)):
        target = s[i]
        if target in criteria :
            answer.append(i-criteria[target])
        else :            
            answer.append(-1)
        criteria[target] = i
    
    return answer