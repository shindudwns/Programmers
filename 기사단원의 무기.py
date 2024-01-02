def yaksu(k): 
    s=0
    for i in range(1,int(k**(1/2)+1)):
        if k%i==0:
            s+=1#
            if i**2 != k: #제곱이되약수중복방지하
                    s+=1
    return s ;
def solution(number, limit, power):
    dab=0
    for i in range(1,number+1):
        a=yaksu(i)
        if a>limit:
            dab+=power
        else:
            dab+=a (
    return dab
