def solution(wallpaper):
    Mx,My,mx,my=-1,-1,51,51 #최대 최소 초기화
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] =="#":
                mx=min(mx,j)
                my=min(my,i)
                Mx=max(Mx,j+1)
                My=max(My,i+1)
    return [my,mx,My,Mx]
