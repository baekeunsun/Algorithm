def findDial(target):
    if target in ['A','B','C']:
        return 3
    if target in ['D','E','F']:
        return 4
    if target in ['G','H','I']:
        return 5
    if target in ['J','K','L']:
        return 6
    if target in ['M','N','O']:
        return 7
    if target in ['P','Q','R','S']:
        return 8
    if target in ['T','U','V']:
        return 9
    if target in ['W','X','Y','Z']:
        return 10
        
alphabet = input()
answer = 0

for a in alphabet :
    answer += findDial(a)
print(answer)