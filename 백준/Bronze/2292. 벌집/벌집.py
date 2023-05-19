# 벌집
N = int(input())
idx = 0
end_num = 1
while True :
    if N <= end_num :
        print(idx+1)
        break
    if N > end_num :
        idx += 1
        end_num += 6*(idx)