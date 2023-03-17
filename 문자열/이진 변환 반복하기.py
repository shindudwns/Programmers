def solution(s):
    cnt,stac,stack=0,0,0
    while (cnt!=1):
        a,cnt="",0
        stac+=1
        for i in range(len(s)):
            if s[i]=="1":
                cnt+=1
            else :
                stack+=1       
        temp=cnt
        while(temp!=0):
            a+=str(temp%2)
            temp//=2
        s=a #사실 뒤집을 필요도 없음
    return [stac,stack]
