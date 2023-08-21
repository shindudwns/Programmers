def solution(elements):
    ele,answer=(elements*2),set()
    for i in range(len(elements)):
        for j in range(len(elements)):
            answer.add(sum(ele[j:j+i+1]))   
    return len(answer)
