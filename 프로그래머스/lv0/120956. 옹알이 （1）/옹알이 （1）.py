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
                else :
                    break
            else :
                break
        continue
    return answer


def solution(babbling):
    c = 0
    for b in babbling:
        for w in [ "aya", "ye", "woo", "ma" ]:
            if w * 2 not in b:
                b = b.replace(w, ' ')
        if len(b.strip()) == 0:
            c += 1
    return c