def solution(babbling):
    can = {"a":"aya", "y":"ye", "w":"woo", "m":"ma"}
    answer = 0
    for i in range(len(babbling)):
        now = babbling[i]
        while now : # now 문자있는 동안
            if now[0] in can :  # 해당하는 단어 시작이 있을 경우
                if now[:len(can[now[0]])] == can[now[0]] :
                    now = now.replace(can[now[0]],"")   # 대체
                    if now :
                        continue
                    else :
                        answer += 1
                else :
                    break
            else :
                break
        continue
    return answer