import sys
sys.stdin = open('안전영역.txt', 'r')


arr = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def BFS(j, x, y):
    Que = [[x, y]]
    while Que:
        v = Que.pop(0)
        for (a, b) in arr:
            dx = v[0] + a
            dy = v[1] + b
            if 0 <= dx < N and 0 <= dy < N and visit[dx][dy] == False and board[dx][dy] != -1:
                visit[dx][dy] = True
                Que.append([dx,dy])

N = int(input())

board = []

for i in range(N):
    board.append(list(map(int, input().split())))
    if i == 0:
        maxH = max(board[i])
    y = max(board[i])
    if y > maxH:
        maxH = y


result = []

for j in range(0, maxH + 1): # 비 내리는 범위
    cnt = 0
    visit = [[False] * N for _ in range(N)]
    for a in range(len(board)):
        for b in range(len(board[a])):
            if board[a][b] == j:
                board[a][b] = -1
                visit[a][b] = True
    for x in range(len(board)): # x y 좌표
        for y in range(len(board[x])):
            if board[x][y] != -1 and visit[x][y] == False:
                visit[x][y] = True
                BFS(j, x, y)
                cnt = cnt + 1
    result.append(cnt)
print(max(result))