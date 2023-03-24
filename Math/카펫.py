def solution(x, y):
    mx=x+y
    t=x//2+2
    for i in reversed(range(t)):
        for j in reversed(range(t)):
            if i*j==mx and (i+j-2)*2==x:
                a=[i,j]
                return a
                break     
