def solution(k, m, score):
    answer,tmp = 0,0
    score.sort(reverse=True) # 내림차순으로 정렬
    while tmp<=len(score)-m:#남은 사과들은 버림
        arr=[] #상자마다 리스트 생성
        for i in range(m):
            arr.append(score[i+tmp])
        answer+=min(arr)*m
        tmp+=m
    return answer
