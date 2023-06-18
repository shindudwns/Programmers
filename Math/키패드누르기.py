def solution(numbers, hand):
    answer=''
       #키패드 위치
    keypad = {'1':(0,0), '2':(0,1), '3':(0,2),
           '4':(1,0), '5':(1,1), '6':(1,2),
           '7':(2,0), '8':(2,1), '9':(2,2),
           '*':(3,0), '0':(3,1), '#':(3,2)
        }
    
    left = keypad['*']   #처음 왼손의 위치
    right = keypad['#']  #처음 오른손의 위치
    
    for i in numbers:
        if i in [1,4,7]:
            answer+='L'
            left=keypad[str(i)]
        elif i in [3,6,9]:
            answer+='R'
            right=keypad[str(i)]
        else:
            le_dis=abs(left[0]-keypad[str(i)][0])+abs(left[1]-keypad[str(i)][1])
            ri_dis=abs(right[0]-keypad[str(i)][0])+abs(right[1]-keypad[str(i)][1])
            if le_dis <ri_dis:
                answer+='L'
                left=keypad[str(i)]
            elif le_dis > ri_dis:
                answer+='R'
                right=keypad[str(i)]
            else:
                if hand=='right':
                    answer+="R"
                    right=keypad[str(i)]
                else:
                    answer+='L'
                    left=keypad[str(i)]
    
    return answer
