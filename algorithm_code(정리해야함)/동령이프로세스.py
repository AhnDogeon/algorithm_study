import sys
import itertools
sys.stdin = open('1767 프로세서 연결.txt', 'r')

diff = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 동-1 남-2 서-3 북-4

def line_count(i, j):
    idx = [[i, j]]
    dir = []
    for (x, y) in diff:
        dx, dy = i + x, j + y
        while 0 <= dx < N and 0 <= dy < N and maxi[dx][dy] == 0:
            if dx == 0 or dx == N - 1 or dy == 0 or dy == N - 1:
                # 동
                if x == 0 and y == 1:
                    dir.append(-1)
                    break
                # 남
                elif x == 1 and y == 0:
                    dir.append(-2)
                    break
                # 서
                elif x == 0 and y == -1:
                    dir.append(-3)
                    break

                # 북
                elif x == -1 and y == 0:
                    dir.append(-4)
                    break
            dx += x
            dy += y
    if len(dir) == 0:
        visit[i][j] = True
    else:
        idx.append(dir)
    return idx

T = int(input())

for t in range(1, T+1):
    N = int(input())

    maxi = [list(map(int, input().split())) for _ in range(N)]

    visit = [[False for _ in range(N)] for _ in range(N)]
    MIN = N + 1
    result = []
    # 시작점에서 갈 수 있는 방향 찾는 로직
    for i in range(1, N-1):
        for j in range(1, N-1):
            if maxi[i][j] == 1 and visit[i][j] == False:
                result.append(line_count(i, j))
    print(result)
    direc = []
    for i in range(len(result)):
        direc.append(result[i][1])
    print(direc)

    for i in range(ddd):
        for j in range(ddd):
            for k in range(ddd):
                for m in range(ddd):
                    result = []
                    result.append(i)
                    result.append(j)
                    result.append(k)
                    result.append(m)


    def forfor(hap, direc):
        if hap == len(direc):
            for i in direc[hap-1]:
                result = []
                for m in for_list: # 좌표값 돌기
                    result.append(m)
            print(result)
        else:
            for j in direc[hap]:
                for_list[hap] = j
                forfor(hap+1, direc)

    for_list = [[0] for _ in range(len(direc))]uuuuuuuuuuuuuuuuuuu # 좌표값
    print(for_list)
    hap = 0
    for i in direc[0]:
        for_list[hap] = i
        forfor(hap,direc)