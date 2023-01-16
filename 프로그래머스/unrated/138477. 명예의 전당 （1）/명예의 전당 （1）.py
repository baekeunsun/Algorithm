def solution(k, score):
    answer = []
    rank = []
    while score:
        target = score.pop(0)
        rank.append(target)
        rank.sort(reverse=True)
        if len(rank) > k :
            rank.pop()
        answer.append(rank[-1])    
    return answer