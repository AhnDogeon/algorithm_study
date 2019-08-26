import sys
sys.stdin = open('input.txt', 'r')
#지원님 풀이
def BFS(S,G):
    visited = [False] * (V+1)
    Dis = [0] * (V+1)
    Q = [S]
    visited[S] = True
    while Q:
        v = Q.pop(0)
        for j in G[v]:
            if not visited[j]:
                Dis[j] = Dis[v]+1
                visited[j] = True
                Q.append(j)j
    return Dis

T= int(input())
for test_case in range(1,T+1):
    V,E = map(int,input().split())
    arr=[]
    G = [[] for _ in range(V+1)]
    for _ in range(E):
        arr.extend(list(map(int, input().split())))
    for i in range(0, len(arr), 2):
        G[arr[i]].append(arr[i+1])
        G[arr[i+1]].append(arr[i])
    S,D = map(int, input().split())
    ans = BFS(S,G)[D]
    print('#{} {}'.format(test_case, ans))