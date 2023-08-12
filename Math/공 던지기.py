def solution(numbers, k):
    numbers*=(2000//len(numbers)+1)
    return numbers[k*2-2]
