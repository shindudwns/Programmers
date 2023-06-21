def solution(s, skip, index):
    answer = ''
    cps=[]
    for i in range(len(s)):
        tmp,stack=index,0
        while tmp:
            if stack==26:
                stack=0
            if ord(s[i])+stack>=122:
                temp=chr(ord(s[i])-26+stack)
            else:
                temp=chr(stack+ord(s[i]))
            if not temp in skip:
                tmp-=1
            stack+=1
        answer+=chr(ord(temp)+1)   
    return answer
