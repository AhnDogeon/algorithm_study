import sys
sys.stdin = open('파이프.txt', 'r')


def DP(x, y, info):
    info = info
    if x == 0 and y > 1:
        if board[x][y] != 1:
            info[x][y][0] = info[x][y - 1][0]
        else:
            info[x][y] = [0, 0, 0]
    if x > 0 and y > 1:
        if board[x][y] != 1:
            info[x][y][0] = info[x][y-1][0] + info[x][y-1][2]
            info[x][y][1] = info[x-1][y][1] + info[x-1][y][2]
            if board[x-1][y] != 1 and board[x][y-1] != 1:
                info[x][y][2] = info[x-1][y-1][0] + info[x-1][y-1][1] + info[x-1][y-1][2]
        else:
            info[x][y] = [0, 0, 0]



N = int(input())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

info = [[[0,0,0] for _ in range(N)] for _ in range(N)]

info[0][1] = [1, 0, 0]

for i in range(len(board)):
    for j in range(len(board[i])):
        DP(i, j, info)
print(sum(info[N-1][N-1]))