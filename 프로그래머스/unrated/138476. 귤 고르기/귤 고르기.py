def solution(k, tangerine):
    sorted_dict = make_dict(tangerine)
    answer = 0
    tmp = 0
    for i in sorted_dict:
        if tmp < k :
            tmp += i
            answer += 1   
    return answer

def make_dict(tangerine):
    my_dict = {}
    while tangerine :
        tmp = tangerine.pop()
        if tmp in my_dict :
            my_dict[tmp] += 1
        else :
            my_dict[tmp] = 1            
    return sorted(my_dict.values(), reverse = True)