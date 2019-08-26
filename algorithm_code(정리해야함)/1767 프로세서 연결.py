import sys
import itertools
sys.stdin = open('1767 프로세서 연결.txt', 'r')


diff = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def DFS(i, j):
    direction = {}
    for (a, b) in diff:
        cnt = 0
        dx = i + a
        dy = j + b
        if board[dx][dy] == 0: # visit이 false인지 true인지 조건 넣어주기
            while 0 <= dx < N and 0 <= dy < N:
                if board[dx][dy] == 0:
                    cnt += 1
                    dx += a
                    dy += b
                else:
                    cnt = 0
                    break
            if cnt != 0:
                direction[(a, b)] = cnt
        elif board[dx][dy] == 1 or board[dx][dy] == 2:
            cnt = 0
            pass
    visit[i][j] = direction

def find_one():
    length = 1
    while length < 5:
        for a in range(len(visit)):
            for b in range(len(visit[a])):
                if len(visit[a][b]) == length:
                    z = wall(a, b, visit[a][b])
                    return z
        else:
            length += 1

def wall(a, b, dict):
    for key, value in dict.items():
        if value == min(dict.values()):
            z = value
            for val in range(value):
                dx = a + key[0]
                dy = b + key[1]
                board[dx][dy] = 2
                a = dx
                b = dy
    return z

def DFS_real():
    visit = []
    for visit_i in range(N):
        visit.append(list([] for _ in range(N)))

    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if board[i][j] == 1:
                DFS(i, j)


T = int(input())


for test_case in range(1, T + 1):
    total = 0
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    visit = []
    for visit_i in range(N):
        visit.append(list([] for _ in range(N)))

    for i in range(1, N - 1):
        for j in range(1, N -1):
            if board[i][j] == 1:
                DFS(i, j)

    iter_list = []
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if len(visit) > 0 and board[i][j] != 0:
                iter_list.append(visit[i][j])
    for _ in range(len(iter_list)):
        DFS_real()
        print(board)
        print(visit)
        total += find_one()
    print(total)