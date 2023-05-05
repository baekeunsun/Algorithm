# 골뱅이 찍기 - 돌아간 ㅍ
N = int(input())
line = []
line.append('@'*N + '   '*N +'@'*N)
line.append('@@@@@'*N)

for _ in range(2):
    for i in range(2):
        for _ in range(N):
            print(line[i])

for _ in range(N):
    print(line[0])
