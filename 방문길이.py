def solution(dirs):
    d={'L':(0,-1),'R':(0,1),'D':(-1,0),'U':(1,0)} #LRDU
    answer = set()
    y,x=0,0
    for i in dirs:
        ny,nx=d[i]
        if abs(y+ny) <= 5 and abs(x+nx) <= 5 :
            answer.add((y,x,y+ny,x+nx))
            answer.add((ny+y,nx+x,y,x))
            y+=ny
            x+=nx
    return len(answer)//2
