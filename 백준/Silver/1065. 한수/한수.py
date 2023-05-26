# 한수
N = int(input())
answer = 0
for i in range(1, N+1):
    if i < 100: # 세자리수가 아니면 무조건 한수
        answer += 1
        continue
    else:
        num_list = list(map(int, str(i)))
        if num_list[0] - num_list[1] == num_list[1] - num_list[2]:
            answer += 1 
    
print(answer)
