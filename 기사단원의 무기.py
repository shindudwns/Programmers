def yaksu(k): 
    s=0
    for i in range(1,int(k**(1/2)+1)):
        if k%i==0:
            s+=1# ㅇㅇ
            if i**2 != k: #제곱이 되는 약수 중복 방지하는 과정
                    s+=1
    return s   
def solution(number, limit, power):
    dab=0
    for i in range(1,number+1):
        a=yaksu(i)
        if a>limit:
            dab+=power
        else:
            dab+=a 
    return dab
