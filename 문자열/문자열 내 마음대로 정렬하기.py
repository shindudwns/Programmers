
def solution(strings, n):
    tmp,answer = [],[]
    for i in strings:
        tmp.append(i[n]+i)
    tmp=sorted(tmp)
    for i in tmp:
        answer.append(i[1:])//asd
    return answer 
