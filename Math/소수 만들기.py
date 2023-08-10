from itertools import combinations, permutations

def sotsu(n):
    for i in range(2,n):
        if n%i==0:
            return 0
    return 1

def solution(nums):
    answer=0
    perm = list(combinations(nums, 3))
    for i in perm :
        if sotsu(sum(i)):
            answer+=1

    return answer
