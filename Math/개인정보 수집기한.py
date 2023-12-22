# def cal(day,tmp):#달력 계산기
#     day[1]+=tmp    
#     if day[1]>12:
#         day[0]+=1
#         day[1]-=12
#     if day[-1]==1:
#         day[-1]=28
#     else:
#         day[-1]-=1
#     return day

def solution(today, terms, privacies):
    answer,dic,stack = [],dict(),0
    for i in terms:
        a= i.split(" ")
        dic[a[0]]=int(a[1])*28
    day=today.split(".")
    day_=int(day[0])*336+(int(day[1])-1)*28+int(day[2])
    for i in range(len(privacies)):
        deadline=privacies[i][:-2].split(".")
        dead=int(deadline[0])*336+(int(deadline[1])-1)*28+int(deadline[2])+(dic[privacies[i][-1]])# 파기 기
        if dead<=day_:
            answer.append(i+1)
    return answer
