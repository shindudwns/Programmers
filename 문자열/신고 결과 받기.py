def solution(id_list, report, k):
    answer = {"muzi":0, "frodo":0, "apeach":0, "neo":0}
    mail = [0] * len(id_list)
    
    report=set(list(report))
    for i in report:
        for j in range(len(i)):
            if i[j]==' ':
                if i[j+1:] in answer:
                    answer[i[j+1:]]+=1
                else:
                    answer[i[j+1:]]=1
    for i in report:
        for j in range(len(i)):
            if i[j]==' ':
                if answer[i[j+1:]]>=k:
                    mail[id_list.index(i[:j])] += 1
    return mail





# def solution(id_list, report, k):
#     answer = [0] * len(id_list)
#     reports = {x : 0 for x in id_list}

#     for r in set(report):
#         reports[r.split()[1]] += 1

#     for r in set(report):
#         if reports[r.split()[1]] >= k:
#             answer[id_list.index(r.split()[0])] += 1

#     return answer
