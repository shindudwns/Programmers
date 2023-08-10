def yaksu(n,m):
    a=1
    for i in range(1,min(n,m)+1):

        if n%i==0 and m%i==0:
            a=i
    return a

def besu(n,m):
    big,small,a=max(n,m),min(n,m),max(n,m)
    while a%small!=0:
        a+=big
    return a

def solution(n, m):
    return [yaksu(n,m),besu(n,m)]
