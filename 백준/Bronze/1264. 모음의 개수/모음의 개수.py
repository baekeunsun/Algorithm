# 모음의 개수

while True:
    line = input()
    if line == '#':	# 입력의 끝
        break
        
    count = 0
    for l in line:
        if l in 'aeiouAEIOU': # 모음이면
            count += 1
    print(count)