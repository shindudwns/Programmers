def solution(dartResult):
    answer = 0
    score=[]
    n=-1
    dartResult = dartResult.replace("10", "A")
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            n+=1
            score.append(int(dartResult[i]))    
        elif dartResult[i]=='A':
            n+=1
            score.append(10)
        elif dartResult[i]=='S':
            continue
        elif dartResult[i]=='D':
            score[n]*=score[n]
        elif dartResult[i]=="T" :
            a=score[n]
            score[n]=a*a*a
        elif dartResult[i]=='#':
            score[n]-=score[n]*2
        elif dartResult[i] == "*":
            if n>0:
                score[n-1]*=2
                score[n]*=2
            else :
                score[n]*=2
        print(score)
    answer=score[0]+score[1]+score[2]
                    
   #* 전 값과 지금값 두배 이벤트
   # 해당 점수 마이너스  
   # *#은 마이너스 두배가 됨
    
    return answer
