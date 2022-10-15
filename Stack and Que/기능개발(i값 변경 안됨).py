def solution(progresses, speeds):
    answer = []
    progresses_day=[]
    for i in range(len(progresses)):
        if (100-progresses[i])%speeds[i]==0:
            progresses_day.append((100-progresses[i])/speeds[i])
        else :
            progresses_day.append((100-progresses[i])//speeds[i]+1)
    check=[num * 0 for num in progresses_day]
    check1=0
    day=0
    t=0
    for i in range(len(progresses_day)):
        stack=0
        now=i
        for j in range(i+1,len(progresses_day)-1):
            if progresses_day[i]>=progresses_day[j]:
                stack+=1
                now=j
            else:
                break
        answer.append(stack+1)
        i=now+1
    return answer
