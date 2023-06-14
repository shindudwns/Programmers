def solution(s):
    answer,stcnt,edcnt,now=0,0,0,1
    start=''
    for i in s:
        if now==1:#시작값 설정
            start=i           
        if start==i:#같으면 stcnt플러스
            stcnt+=1
        else:       #틀리면 edcnt플러스
            edcnt+=1
        if stcnt==edcnt:#같으면 초기화 후 answer +1
            now,stcnt,edcnt=0,0,0
            answer+=1   
        now+=1
    if not now ==1: # 끝까지 안나눠 졌을때 +1
        answer+=1
    return answer
