def solution(n):
    answer = 1
    for i in range(1,n//2+1):# 이 부분 범위만 바꿔주니 해결됐다.
        temp=i
        sum=0
        while(n>sum):
            sum+=temp
            temp+=1
            if sum==n:
                answer+=1
    return answer
