def solution(board):
    bomb,answer=[],0
    dx,dy=[-1,0,1,-1,1,-1,0,1],[-1,0,1,-1,1,-1,0,1]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==1:
                bomb.append((i,j))
    for x,y in bomb:
        for i in range(8):
            ax=x+dx[i]
            ay=y+dy[i]
            if 0<=ax<len(bomb) and 0 <= ay < len(bomb):
                bomb[ax][ay]=2
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==0:
                answer+=1
    return answer
