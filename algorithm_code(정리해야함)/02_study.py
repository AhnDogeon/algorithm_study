import sys
sys.stdin = open('input_2.txt', 'r')

def DFS(x, y):
    if D[x][y] >= D[ex][ey]: return
    for (dx, dy) in diff:
        tx, ty = x + dx, y + dy
        if tx < 0 or tx == N or ty < 0 or ty == N or maze[tx][ty] == '1':
            continue
        if D[tx][ty] > D[x][y] + 1:
            D[tx][ty] = D[x][y] + 1
            DFS(tx, ty)
diff = [(0, 1), (0, -1), (1, 0), (-1, 0)]
INF = 0xffffff
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    D = [[INF for _ in range(N)] for _ in range(N)]
    sx = sy = ex = ey = 0
    maze = []
    for i in range(N):
        maze.append(input())
        for j in range(N):
            if maze[i][j] == '2':
                sx, sy = i, j
            if maze[i][j] == '3':
                ex, ey = i, j
    D[sx][sy] = 0
    DFS(sx, sy)
    ans = 0
    if D[ex][ey] < INF:
        ans = D[ex][ey] - 1
    print("#%d %d" % (test_case, ans))