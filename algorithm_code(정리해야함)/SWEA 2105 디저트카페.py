import sys
sys.stdin = open('SWEA 2105 디저트카페.txt', 'r')
T = int(input())

diff = [(-1, -1, -2), (-1, 1, -3), (1, -1, -4), (1, 1, -5)]
def DFS(sx, sy, i, j, result, tx, ty, dz):
    global real, MAX
    for (x, y, z) in diff:
        dx, dy = i + x, j + y
        if sx == dx and sy == dy and z + dz != -7:
            real.append(result)
            if len(result) > MAX:
                MAX = len(result)
        if 0 <= dx < N and 0 <= dy < N and visit[dx][dy] == False and cafe[dx][dy] not in result:
            visit[dx][dy] = True
            DFS(sx, sy, dx, dy, result + [cafe[dx][dy]], x, y, z)
    return



for t in range(1, T+1):
    N = int(input())

    cafe = [list(map(int, input().split())) for _ in range(N)]
    MAX = 0
    real = []
    for i in range(N):
        visit = [[False for _ in range(N)] for _ in range(N)]
        for j in range(N):
            result = [cafe[i][j]]
            sx = i
            sy = j
            dz = tx = ty = 0
            DFS(sx, sy, i, j, result, tx, ty, dz)
    print('#{} {}'.format(t, MAX))
    for i in range(len(real)):
        if len(real[i]) == MAX:
            print(real[i])