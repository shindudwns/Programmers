def solution(s):
    answer=''
    s=s.lower()
    s=list(s)   
    s[0]=s[0].upper()
    for i in range(len(s)):
        if s[i-1] == " " :
            s[i]=s[i].upper()
        answer += s[i]
    return answer
