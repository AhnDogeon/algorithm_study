def solution(vote):
    answer = 0
    real_visit = [False] * len(vote)
    visit = [False] * len(vote)
    for start in range(len(real_visit)):
        if real_visit[start] == False:
            result = DFS(start, vote, visit, real_visit, start, False)
            if result == 3:
                answer += 1
            else:
                pass
        visit = [False] * len(vote)
    return answer


def DFS(v, vote, visit, real_visit, start, isend):
    real_visit[v] = True
    if v == start and isend == True:
        return visit.count(True)
    else:
        if visit[v] == False:
            visit[v] = True
            k = DFS(vote[v]-1, vote, visit, real_visit, start, True)
        elif visit[v] == True:
            true_cnt = visit.count(True)
            return true_cnt
        else:
            k = 0
        return k

dap  = solution([2,3,1,3,4])
print(dap)