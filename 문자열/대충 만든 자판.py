def solution(keymap, targets):
    answer=[]
    for i in targets:
        a=len(i)
        for j in i:
            mn=101
            for k in keymap:
                if j in k:
                    mn=min(mn,k.index(j))
                    # print(j,k.index(j))
            if mn==101:
                # print("최종값",j,mn)
                a=-1
                break
            else:
                a+=mn
        answer.append(a)
    
    return answer
