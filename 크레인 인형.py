def solution(board, moves)
    answer= 0
    arr=[] # 바구니 리스트
    for i in range(len(moves)):
        for j in range(len(board[0])):
            if not board[j][moves[i]-1]==0:
                if arr and arr[-1] == board[j][moves[i]-1]  :
                    del arr[-1]
                    answer+=2
                else:
                    arr.append(int(board[j][moves[i]-1]))
                board[j][moves[i]-1]=0
                break
    return answer
