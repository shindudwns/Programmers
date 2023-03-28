def solution(k, tangerine):
    num={}
    for i in tangerine:
        if i in num:
            num[i]+=1
        else :
            num[i]=1   
    arr=list(num.values())
    arr.sort(reverse=True)
    answer,stack=0,0
    for i in arr:      
        if stack>=k:         
            break
        else:
            stack+=i
            answer+=1
    return answer
