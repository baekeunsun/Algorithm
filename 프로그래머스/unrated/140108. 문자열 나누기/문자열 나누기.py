def solution(s):
    answer = 0
    first = s[0]
    same = 0
    diff = 0
    while s :
        if same != 0 and same == diff :
            same = 0
            diff = 0
            answer += 1
            first = s[0]
        target = s[0]
        s = s[1:]
        if first == target :
            same += 1
        else :
            diff += 1
            
    return answer + 1