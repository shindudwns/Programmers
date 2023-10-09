def solution(n, lost, reserve):
    
    arr=[0 * i+1 for i in range(n)]    
    for i in range(len(lost)):
        arr[lost[i]-1]-=1
    for i in range(len(reserve)):
        arr[reserve[i]-1]+=1
    if arr[n-1]>0:
        if arr[n-1]==2 and arr[n-2]==0:
            arr[n-2]=1
    for i in range(n-2,0,-1):
        if arr[i]<=1:
            continue
        if arr[i]==2:
            if arr[i+1]==0:
                arr[i+1]=1
                arr[i]=1
            elif arr[i-1]==0:
                arr[i-1]=1
                arr[i]=1
    if arr[0]==2 and arr[1]==0:
        arr[1]=1
    return n - arr.count(0)
