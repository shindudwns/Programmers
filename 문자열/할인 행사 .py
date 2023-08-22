from collections import Counter
def solution(want, number, discount):
    stack = 0
    for i in range(len(discount) - 9):
        stack += 1
        counter = Counter(discount[i:i+10])
        for item, count in zip(want, number):
            if counter[item] != count:
                stack -= 1
                break
    return stack
