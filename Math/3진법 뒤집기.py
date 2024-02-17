def solution(n):
    tmp,answer = '';
    while n>0:
        tmp+=str(n%3)
        n//=3;
    for i in range(len(tmp)):ㄹ
        answer+=int(tmp[i])*pow(3,len(tmp)-i-1)
    return answer
