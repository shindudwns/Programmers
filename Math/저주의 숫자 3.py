def check(a):
    if a%3==0 or a%10==3 or '3' in list(str(a)):
        return check(a+1)
    else:
        return a+1

def solution(n):
    answer = 1
    for i in range(n):
        answer = check(answer)
    return answer-1
