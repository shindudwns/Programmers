def solution(s):
    arr=[s[0]]
    for i in range(1,len(s)):
        if arr and s[i]==arr[-1]  :
            arr.pop()
        else:
            arr.append(s[i])
    return len(arr)==0 and 1 or 0
