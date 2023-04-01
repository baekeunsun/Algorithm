# Numbersrebmun
def makeNum(name):
    numName = []
    for i in range(len(name)):
        if name[i] <= 'C':
            numName.append(2)
        elif name[i] <= 'F':
            numName.append(3)
        elif name[i] <= 'I':
            numName.append(4)
        elif name[i] <= 'L':
            numName.append(5)
        elif name[i] <= 'O':
            numName.append(6)
        elif name[i] <= 'S':
            numName.append(7)
        elif name[i] <= 'V':
            numName.append(8)
        else:
            numName.append(9)
    return numName

for _ in range(int(input())):
    name = makeNum(input().upper())
    if name ==name[::-1]:
        print("YES")
    else:
        print("NO")



