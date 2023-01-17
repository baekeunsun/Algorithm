def solution(food):
    answer = '0'
    for i in range(len(food)-1,-1,-1):
        tmp = food[i]//2
        answer = str(i)*tmp + answer + str(i)*tmp
        
    return answer