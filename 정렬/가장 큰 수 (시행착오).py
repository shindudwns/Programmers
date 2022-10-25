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
