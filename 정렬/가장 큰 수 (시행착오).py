import itertools
def solution(numbers):
    array=[]
    aa=[]
    for i in numbers:
        aa.append(str(i))
    print(numbers)
    aaa = itertools.permutations(aa, len(aa))
    ans = [int(''.join(i)) for i in aaa]
    ans.sort()
    answer=str(ans[len(ans)-1])
    return answer
  
  #순열을 이용해 풀었으나 시간초과가 남
