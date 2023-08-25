def habseong(n):
    for i in range(2,n):
        if n%i==0:
            return 1
    return 0
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if habseong(i):
            answer+=1
    return answer
