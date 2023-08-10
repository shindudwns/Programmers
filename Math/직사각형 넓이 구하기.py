def solution(dots):
    ax,ay,bx,by=-256,-256,256,256
    
    ax=max(dots)[0]
    bx=min(dots)[0]
    ay=max(dots)[1]
    by=min(dots)[1]
    
    return (ay-by)*(ax-bx)
