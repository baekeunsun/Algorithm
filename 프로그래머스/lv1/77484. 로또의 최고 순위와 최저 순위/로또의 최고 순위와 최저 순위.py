def solution(lottos, win_nums):
    lottos.sort(reverse=True)
    win_nums.sort(reverse=True)
    score = 0
    zero = 0
    
    i = 0
    j = 0
    while i != 6 and j != 6:
        if lottos[i] == win_nums[j] :
            score += 1
            i += 1
            j += 1
        elif lottos[i] > win_nums[j]:
            i += 1
        else :
            j += 1
            
    zero = lottos.count(0)
            
    Min = 7 - (score+zero)
    Max = 7 - score
    if Min >= 7 :
        Min = 6
    if Max >= 7 :
        Max = 6
        
    answer = [Min, Max ]
    return answer