def solution(n):
    n=list(str(n))
    n.sort(reverse=True)
    answer = ''
    for i in n:
        answer+=i
    return int(answer)
