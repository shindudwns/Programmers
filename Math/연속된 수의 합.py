def solution(num, total):
    answer,tmp,tp = [],0,total//num
    if num%2==0:
        tmp=total//num-(num//2-1)
    else:
        tmp=total//num-(num//2)   
    for i in range(num):
        answer.append(tmp+i)      
    return answer

// 최적화


def solution(num, total):
    if num%2==0:
        return [i+total//num-(num//2-1) for i in range(num)]
    else:
        return [i+total//num-(num//2)for i in range(num)]
