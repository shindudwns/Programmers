def solution(progresses, speeds):
    answer = []
    progresses_day=[] #걸리는 시간 기록 리스트
    for i in range(len(progresses)):#걸리는 시간 계산 후 리스트에 넣는 과정
        if (100-progresses[i])%speeds[i]==0:
            progresses_day.append((100-progresses[i])/speeds[i])
        else :
            progresses_day.append((100-progresses[i])//speeds[i]+1)
    for i in range(len(progresses_day)):
        stack=0 #앞에서 뒤에 같은 작업날에 낼 수 있는 지 쌓아주는 stack값
        now=i #i값 변경을 위한 변수 선언
        for j in range(i+1,len(progresses_day)):
            if progresses_day[i]>=progresses_day[j]:#다음 작업물도 같이 낼 수 있을 때
                stack+=1 
                now=j #i값을 j값으로 건너뛰기위해 저장
            else:
                break
        answer.append(stack+1)
        i=now+1#i값 변경(하지만 변경이 반영이 안됨).
    return answer
