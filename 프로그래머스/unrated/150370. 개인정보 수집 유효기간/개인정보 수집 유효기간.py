def solution(today, terms, privacies):
    answer = []
    today = list(map(int,today.split(".")))
    dictionary = makeDict(terms)    
        
    for i in range(len(privacies)):
        date, term = map(str, privacies[i].split())
        date = list(map(int,date.split(".")))
        
        date[1] = date[1] + dictionary[term]
        if date[1] > 12 :
            date[0] += date[1]//12
            date[1] = date[1]%12
        if date[1] == 0:
            date[1] = 12
            date[0] -= 1
            
        if compareDate(today, date) :
            answer.append(i+1) 
    return answer

def makeDict(terms) :
    dictionary = dict()
    while terms:
        i,j = map(str,terms.pop().split())
        dictionary[i] = int(j)
    return dictionary

def compareDate(today,date) :
    for i in range(3):
        if today[i] > date[i]:
            return True
        if today[i] < date[i] :
            return False
        if i == 2:
            return True