def solution(s):
    answer = [-1]
    for i in range(1,len(s)):
        if s[i] in s[:i]:
            for j in reversed(range(len(s[:i]))):
                if s[i]==s[j]:
                    answer.append(i-j)
                    break
        else:
            answer.append(-1)     
    return answer
