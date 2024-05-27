def blackjack(N, M, cards):
    max_sum = 0
    # 모든 가능한 3장 카드 조합을 탐색
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                current_sum = cards[i] + cards[j] + cards[k]
                # 현재 조합의 합이 M을 넘지 않으면서 최대 합을 갱신
                if current_sum <= M:
                    max_sum = max(max_sum, current_sum)
    return max_sum

# 입력 받기
N, M = map(int, input().split())
cards = list(map(int, input().split()))

# 결과 출력
print(blackjack(N, M, cards))
