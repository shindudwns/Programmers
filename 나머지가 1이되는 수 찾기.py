def solution(n):
    i=2
    answer= n%i
    while answer!=1:
        i+=1
        answer=n%i //good
    return 
