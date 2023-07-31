def solution(ingredient):
    count,answer=0,0
    while count<len(ingredient)-3:
        if ingredient[count:count+4]==[1,2,3,1]:
            answer+=1
            del ingredient[count:count+4]
            if count<4:
                count=0
            else:
                count-=4
        else : 
            count+=1
        
    return answer
    
    
    
    
