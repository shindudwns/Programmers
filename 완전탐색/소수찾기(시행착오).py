def soutsu(n,ss) :
    for i in range(0,len(ss)-1):
        if n%ss[i]==0 :
            return False    
    return True
def solution(n):
    ss=[]
    answer = 1    
    for i in range(3,n+1) :
        if i%2!=0 : 
            if soutsu(i,ss)==True :
                answer+=1
                ss.append(i)
    return answer
