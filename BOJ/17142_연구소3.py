import sys
sys.stdin = open('17142_연구소3.txt', 'r')


N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
visit = [[False] * N for _ in range(N)]

virus = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            virus.append([i,j])
print(virus)
number_list = []

for q in range(len(virus)):
    for w in range(q+1, len(virus)):
        for e in range(w+1, len(virus)):
            number_list.append([q, w, e])

diff = [(0, -1), (0, 1), (-1, 0), (1, 0)]
def BFS(x, y):
    visit = [[False] * N for _ in range(N)]
    copy_board[x][y] = 0
    visit[x][y] = True
    Q = [[x, y]]
    while Q:
        v = Q.pop(0)
        for (a, b) in diff:
            dx, dy = v[0] + a, v[1] + b
            if 0 <= dx < N and 0 <= dy < N and visit[dx][dy] == False and copy_board[dx][dy] == 0:
                visit[dx][dy] = True
                if copy_board[dx][dy] >= copy_board[v[0]][v[1]] + 1 and [dx, dy] not in virus:
                    copy_board[dx][dy] = copy_board[v[0]][v[1]] + 1
                elif copy_board[dx][dy] == 0:
                    copy_board[dx][dy] = copy_board[v[0]][v[1]] + 1
                Q.append([dx, dy])
    copy_board[x][y] = '*'


for number in number_list:
    copy_board = []
    for i in range(N):
        copy_list = []
        for j in range(N):
            if board[i][j] == 1:
                copy_list.append('-')
            elif board[i][j] == 2:
                copy_list.append(0)
            else:
                copy_list.append(board[i][j])
        copy_board.append(copy_list)

    BFS_list = [[0] * N for _ in range(N)]

    BFS(virus[number[0]][0], virus[number[0]][1])
    print('===========바이러스1=====================')
    for m in range(N):
        for n in range(N):
            print(copy_board[m][n], end=' ')
        print()
    print('======================================')
    BFS(virus[number[1]][0], virus[number[1]][1])
    print('===========바이러스2=====================')
    for m in range(N):
        for n in range(N):
            print(copy_board[m][n], end=' ')
        print()
    print('======================================')
    BFS(virus[number[2]][0], virus[number[2]][1])



    print('===========바이러스3=====================')
    for m in range(N):
        for n in range(N):
            print(copy_board[m][n], end=' ')
        print()
    print('======================================')




