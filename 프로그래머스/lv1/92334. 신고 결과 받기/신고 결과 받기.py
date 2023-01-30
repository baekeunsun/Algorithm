def report_processing(id_list, report): # 신고 횟수(len), 나를 신고한사람
    reportList = {id : set() for id in id_list}
    for nameList in report :
        reportFrom, reportTo = map(str,nameList.split(" "))
        reportList[reportTo].add(reportFrom)
    return reportList

def stop(reportList,k):
    stopList =[]
    for nowReport in reportList:
        if len(reportList[nowReport]) >= k : # 신고 당한 횟수가 k 이상이면
            stopList.append(nowReport)
    return stopList

def answer(stopList,id_list,reportList):
    answerList = dict.fromkeys(id_list,0)
    for target in stopList :
        for i in reportList[target]:
            answerList[i] += 1
    return list(answerList.values())

def solution(id_list, report, k):
    reportList = report_processing(id_list,report)
    stopList = stop(reportList,k)
    return answer(stopList,id_list,reportList)