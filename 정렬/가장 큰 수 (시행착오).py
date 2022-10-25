import itertools
def solution(numbers):
    array=[]
    aa=[]
    for i in numbers:
        aa.append(str(i))
    aaa = itertools.permutations(aa, len(aa))
    ans = [int(''.join(i)) for i in aaa]
    ans.sort(reverse=True)
    answer=str(ans[0])
    return answer
  
  #순열을 이용해 풀었으나 시간초과가 남
  #인터넷을 찾아보니 "permutations 함수는 시간복잡도가 O(n!) 혹은 O(nr)으로 코딩테스트에 쓰기에는 적합하지 않습니다." 라네요

 def vs(a,b):
    c=str(a)+str(b)
    d=str(b)+str(a)
    if int(c>d):
        return a
    else :
        return b  
def solution(numbers):
    answer = ''
    at = 1
    numbers.sort(reverse=True)
    check=[0 for num in numbers]
    tmp=0
    check_i=0
    mx=numbers[check_i]
    while tmp<len(numbers):
        mx=-1
        for j in range (0,len(numbers)):
            if check[j]==0:
#                             if check[j]==0:  9일때 스킵 넣어도 
#                 if numbers[j]==9:
#                     check_i=j
#                     mx=numbers[j]
#                     break
#                 else:
#                     k=mx
#                     mx= vs(mx,numbers[j])
#                     if mx==numbers[j]:
#                         check_i=j
                k=mx
                mx= vs(mx,numbers[j])
                if mx==numbers[j]:
                    check_i=j
        check[check_i]=1
        tmp+=1
        answer+=str(mx)
    if int (answer) == 0:
        answer='0'
    return answer

#두 번째 시간초과 66점 
