def solution(n):
    tmp,answer = '',0
    while n>0:
        tmp+=str(n%3)
        n//=3
    for i in range(len(tmp)):
        answer+=int(tmp[i])*pow(3,len(tmp)-i-1)
    return answer
