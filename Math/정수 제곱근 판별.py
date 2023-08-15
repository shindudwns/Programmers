import math 
def solution(n):
    if math.sqrt(n)-int(math.sqrt(n))==0.0:
        return (math.sqrt(n)+1)**2
    else:
        return -1



// 최적화 코드



import math 
def solution(n):
    return math.sqrt(n)-int(math.sqrt(n))==0.00 and (math.sqrt(n)+1)**2 or -1
