def solution(survey, choices):
    answer=''
    dict={'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0,}
    for i in range(len(choices)):
        if choices[i] <4:
            dict[survey[i][0]]+=abs(choices[i]-4)
        else:
            dict[survey[i][1]]+=abs(choices[i]-4)
    if dict['R']<dict['T']:
        answer+='T'
    else:
        answer+='R'
    if dict['C']<dict['F']:
        answer+='F'
    else:
        answer+='C'
    if dict['J']<dict['M']:
        answer+='M'
    else:
        answer+='J'
    if dict['A']<dict['N']:
        answer+='N'
    else:
        answer+='A'
    return answer
