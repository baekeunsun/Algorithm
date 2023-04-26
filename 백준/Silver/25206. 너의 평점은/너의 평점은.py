# 너의 평점은
total = 0
count = 0.0
score = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0': 1.0, 'F':0.0 }
for _ in range(20):
    grade = list(map(str,input().split(' ')))
    if grade[2] == 'P' :
        continue
    else :
        total += float(score.get(grade[2])) * float(grade[1])
        count += float(grade[1])
try :
    print('%.6f' %(total/count))
except ZeroDivisionError:
    print(0)
