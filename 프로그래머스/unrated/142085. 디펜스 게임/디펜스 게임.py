# n 병사 수 , k 무적권 수, enemy 적등장
import heapq

def solution(n, k, enemy):        
    if k >= len(enemy) :
        return len(enemy)
    
    answer = 0
    game = []
    tmp = 0
    
    for i in range(len(enemy)) :
        heapq.heappush(game,-enemy[i])
        if n >= enemy[i] :
            n -= enemy[i]   # 싸움
            answer += 1
        else :
            n -= enemy[i]
            if k > 0:   # 무적권 사용
                n += -heapq.heappop(game)
                k -= 1
                answer += 1
            else :  # 무적권 사용할 수 X -> 종료
                break        
    return answer