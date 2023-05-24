from collections import deque

def solution(cards1, cards2, goal):
    cards1=deque(cards1)
    cards2=deque(cards2)
    for i in range(len(goal)):
        if  cards1 and cards1[0]==goal[i] : #해당 값이 있는지 체크를 잘 해줘야함 que라서
            cards1.popleft()    
        elif  cards2 and cards2[0]==goal[i]  :
            cards2.popleft()
        else:           
            return "No"       
    return "Yes"
