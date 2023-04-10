# 그룹 단어 체커
answer = 0
N = int(input())
for _ in range(N):
    word = input()
    pre = word[0]
    alpha = set(pre)
    for tmp in word[1:] :
        if tmp == pre or tmp not in alpha :
            pre = tmp
            alpha.add(tmp)
        else :
            answer += 1
            break
print(N-answer)
