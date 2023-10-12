def cal(day,tmp):#달력 계산기
    day[1]+=tmp    
    if day[1]>12:
        day[0]+=1
        day[1]-=12
    if day[-1]==1:
        day[-1]=28
    else:
        day[-1]-=1
    return day

def solution(today, terms, privacies):
    answer,dic,stack = [],dict(),0
    for i in terms:
        a= i.split(" ")
        dic[a[0]]=int(a[1])
    day=today.split(".")
    day[0]=int(day[0])
    day[1]=int(day[1])
    day[2]=int(day[2])
    for i in range(len(privacies)):
        stack=0
        tmp = dic[privacies[i][-1]] # 파기 기한
        deadline=privacies[i][:-2].split(".")
        deadline[0]=int(deadline[0])
        deadline[1]=int(deadline[1])
        deadline[2]=int(deadline[2])
        deadline=cal(deadline,tmp) 
        # print(day , deadline)
        for j in range(3):
            if deadline[j]<day[j]:
                answer.append(i+1)
            elif deadline[j]>day[j]:
                break
    return answer



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
        dic[a[0]]=int(a[1]*28)
    day=today.split(".")
    day_=day[0]+str(int(day[1])*28+int(day[2]))
    for i in range(len(privacies)):
        stack=0
        tmp = dic[privacies[i][-1]] # 파기 기한
        deadline=privacies[i][:-2].split(".")
        dead=deadline[0]+str(int(deadline[1])*28+int(deadline[2]))
        if int(dead)<int(day_):
            answer.append(i+1)
        print(day_,dead)
    # day[0]=int(day[0])
    # day[1]=int(day[1])
    # day[2]=int(day[2])
    # day_=(day[1]*28)+day[2]
    # for i in range(len(privacies)):
    #     stack=0
    #     tmp = dic[privacies[i][-1]] # 파기 기한
    #     deadline=privacies[i][:-2].split(".")
    #     deadline[0]=int(deadline[0])
    #     deadline[1]=int(deadline[1])
    #     deadline[2]=int(deadline[2])
    #     deadline=cal(deadline,tmp) 
    #     if deadline[0] < day[0] :
    #         answer.append(i+1)
    #     elif deadline[0] > deadline[1]:
    #         continue
    #     else:
    #         if sum(deadline[1]*28+deadline[2])<day_:
    #             answer.append(i+1)
    #     print(int(sum(deadline[1]*28+deadline[2])),day_)
    return answer
//1차 수정본
