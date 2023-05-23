def solution(a, b):
    cal=[31,29,31,30,31,30,31,31,30,31,30,31]
    day=['FRI','SAT','SUN','MON','TUE','WED','THU']
    sum=0
    for i in range(a-1):
        sum+=cal[i]
    return day[(sum+b)%7-1]
