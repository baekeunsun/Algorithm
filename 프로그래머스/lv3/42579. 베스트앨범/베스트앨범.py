def solution(genres, plays):
    ans = []
    n = len(genres)
    Genre = {}
    
    # 장르같은 순, 재생횟수 큰 순, 고유번호 낮은 순으로 저장
    total = [[genres[i],plays[i],i] for i in range(n)]
    total = sorted(total, key=lambda x : (x[0], -x[1], x[2]))
    
    # 장르별 재생횟수 dic에 저장
    for i in total :
        if i[0] not in Genre:   #i[0]이 Genre key값에 존재하는지
            Genre[i[0]] = i[1]
        else :
            Genre[i[0]] += i[1]
    
    # Genre dict을 key 내림차순으로 정렬, [()] 형태로 변환
    Genre = sorted(Genre.items(), key=lambda x : -x[1])
    
    # ans에 각 장르 두개 씩 추가
    for i in range(len(Genre)):
        tmp = 0
        for j in range(n):
            if (Genre[i][0] == total[j][0]) and (tmp < 2) :
                ans.append(total[j][2])
                tmp += 1

    return ans