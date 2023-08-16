def solution(num):
    answer,stack = 0,0
    while num!=1 and stack<501:
        if num %2==0:
            num//=2
        else:
            num=num*3+1
        stack+=1
    return stack>500 and -1 or stack
