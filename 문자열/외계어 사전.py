def solution(spell, dic):
    for i in range(len(dic)):
        stack=0
        dic[i]=set(dic[i])
        for j in dic[i]:
            if j in spell:
                stack+=1
        if stack==len(spell):
            answer=1
            break
        else:
            answer=2
    return answer
