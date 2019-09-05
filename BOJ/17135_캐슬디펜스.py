import sys
sys.stdin = open('17135_캐슬디펜스.txt', 'r')
from copy import deepcopy

N, M, D = map(int, input().split())

copy_board = [list(map(int, input().split())) for _ in range(N)]
copy_board.append([0] * M)
board = deepcopy(copy_board)
order = []

for x in range(M):
    for y in range(x+1, M):
        for z in range(y+1, M):
            order.append([x, y, z])
# print(order)

diff = [(-1, 0), (0, 1), (0, -1)]


def BFS(x, y):
    global dap
    visit = [[False] * M for _ in range(N)]
    visit.append([True] * M)
    Dis = [[0] * M for _ in range(N+1)]
    Que = [[x, y]]
    result = []
    current_Dis = 0
    while Que:
        v = Que.pop(0)
        for (a, b) in diff:
            dx, dy = v[0] + a, v[1] + b
            if 0 <= dx < N and 0 <= dy < M and visit[dx][dy] == False:
                visit[dx][dy] = True
                Dis[dx][dy] = Dis[v[0]][v[1]] + 1
                Que.append([dx, dy])
        # print('============디버깅==============')
        # print('v는', v)
        # for di in range(N):
        #     for si in range(M):
        #         print(Dis[di][si], end=' ')
        #     print()
        # print('================================')
        if Dis[v[0]][v[1]] != current_Dis:
            for dd in range(N):
                for ss in range(M):
                    if Dis[dd][ss] == current_Dis - 1 and board[dd][ss] == 1 and visit[dd][ss] == True:
                        result.append([dd, ss])
            current_Dis = Dis[v[0]][v[1]] + 1
            if len(result) > 0:
                small = 0xffff
                for i in result:
                    if i[1] <= small:
                        small = i[1]
                        answer = i
                # print(x, y, '가', answer, '죽임')
                if answer not in dap:
                    dap.append(answer)
                break
            result = []



def down():
    for n in range(N-1, -1, -1):
        for m in range(M):
            if board[n][m] == 1:
                if n == N - 1:
                    board[n][m] = 0
                else:
                    board[n+1][m] = 1
                    board[n][m] = 0

maxtotal = 0
for arr in order:
    board = deepcopy(copy_board)
    total = 0
    time = 0
    # print('==========================================')
    # print('arr은', arr)
    while time <= N:
        time += 1
        dap = []
        for idx in arr:
            BFS(N, idx)
        # print(dap)
        if dap:
            for d in dap:
                board[d[0]][d[1]] = 0
                total += 1

        down()
    # print(total)
    if maxtotal < total:
        maxtotal = total
print(maxtotal)

