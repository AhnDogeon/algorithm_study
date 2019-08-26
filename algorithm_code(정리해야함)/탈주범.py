eimport sys
sys.stdin = open('탈주범.txt', 'r')

T = int(input())



def BFS(x, y):
    global time_cnt
    time_cnt += 1
    Q = [[x, y]]
    visit[x][y] = True
    dis[x][y] = 1
    while Q:
        v = Q.pop(0)
        diff = direc(v[0], v[1])
        if dis[v[0]][v[1]] + 1 > L:
            break
        for (a, b) in diff:
            dx = v[0] + a
            dy = v[1] + b
            if 0 <= dx < N and 0<= dy < M:
                input = check(dx, dy, a, b)
                if board[dx][dy] != 0 and visit[dx][dy] == False and input == True:
                    visit[dx][dy] = True
                    dis[dx][dy] = dis[v[0]][v[1]] + 1
                    Q.append([dx, dy])
                    for i in range(N):
                        for j in range(M):
                            print(dis[i][j], end=' ')
                        print()
                    print('--------------------------------------------------------------------')

def direc(x, y): # 현재 진행 방향
    if board[x][y] == 1:
        return [(0, 1), (1, 0), (0, -1), (-1, 0)]
    if board[x][y] == 2:
        return [(-1, 0), (1, 0)]
    if board[x][y] == 3:
        return [(0, -1), (0, 1)]
    if board[x][y] == 4:
        return [(-1, 0),(0, 1)]
    if board[x][y] == 5:
        return [(1, 0), (0, 1)]
    if board[x][y] == 6:
        return [(1, 0),(0, -1)]
    if board[x][y] == 7:
        return [(-1, 0),(0, -1)]

def check(dx, dy, a, b):
    if board[dx][dy] == 1:
        return True
    if board[dx][dy] == 2:
        if (a, b) in [(-1, 0), (1, 0)]:
            return True
        else:
            return False
    if board[dx][dy] == 3:
        if (a, b) in[(0, -1), (0, 1)]:
            return True
        else:
            return False
    if board[dx][dy] == 4:
        if (a, b) in [(1, 0),(0, -1)]:
            return True
        else:
            return False
    if board[dx][dy] == 5:
        if (a, b) in [(-1, 0), (0, -1)]:
            return True
        else:
            return False
    if board[dx][dy] == 6:
        if (a, b) in [(-1, 0), (0, 1)]:
            return True
        else:
            return False
    if board[dx][dy] == 7:
        if (a, b) in [(1, 0), (0, 1)]:
            return True
        else:
            return False

for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    # for i in range(N):
    #     for j in range(M):
    #         print(board[i][j], end=' ')
    #     print()
    #
    # print('===============================================================')
    visit = [[False] * (M) for _ in range(N)]
    dis = [[0] * (M) for _ in range(N)]
    time_cnt = 0
    BFS(R, C)
    result = 0
    for n in range(N):
        for m in range(M):
            if dis[n][m] > 0:
                result += 1
    # print('#{} {}'.format(test_case, result))