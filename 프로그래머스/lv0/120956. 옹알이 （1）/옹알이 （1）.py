def solution(babbling):
    can = {"a":"aya", "y":"ye", "w":"woo", "m":"ma"}
    answer = 0
    for now in babbling:
        while now : # now 문자있는 동안
            if now[0] in can :  # 해당하는 단어 시작이 있을 경우
                if now[:len(can[now[0]])] == can[now[0]] :
                    now = now.replace(can[now[0]],"")   # 대체
                    if now :
                        continue
                    answer += 1
                    break
                break
            break
    return answer


def solution(babbling):
    answer = 0
    for now in babbling:
        for word in [ "aya", "ye", "woo", "ma" ]:
            if word * 2 not in now:
                now = now.replace(word, ' ',1)
        if len(now.strip()) == 0:
            answer += 1
    return answer
