def solution(a,b):
    sum=0
    a.sort()
    b.sort(reverse=True)
    print(a,b)
    for i in range(len(a)):
        sum+=a[i]*b[i]
    return sum
