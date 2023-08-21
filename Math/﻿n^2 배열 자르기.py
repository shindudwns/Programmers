def solution(n, left, right):
    start=int((left+1)/n-1)
    end=int((right+1)/n-1)
    print(start,end)
    arr,stack = [],0
    for i in range(start,end+2):
        for j in range(n):
            if i*n+j>=left and i*n+j<=right:
                arr.append(max(i,j)+1)      
    return arr
