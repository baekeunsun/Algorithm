def solution(common):
    return arithmetic(common)

def arithmetic(common):
    tmp = common[1] - common[0]
    for i in range(1,len(common)-1) :
        if common[i+1] != common[i] + tmp :
            return geometric(common)
    return common[-1] + tmp

def geometric(common) :
    tmp = common[1]//common[0]
    for i in range(1,len(common)-1) :
        if common[i+1] != common[i] * tmp :
            return 0
    return common[-1] * tmp
