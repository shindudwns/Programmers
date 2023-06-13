def solution(lottos, win_nums):
    answer = []
    cnt=7
    tmp=0
    for i in lottos:
        if i in win_nums:
            cnt-=1
        elif i==0:
            tmp+=1
    if cnt -tmp>=6:
        answer.append(6)
    else:
        answer.append(cnt-tmp)
    if cnt>=6:
        answer.append(6)
    else:
        answer.append(cnt)
    return answer
