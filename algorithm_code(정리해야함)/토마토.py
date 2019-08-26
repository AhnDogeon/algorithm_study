import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

M, N = map(int, input().split())

farm = [list(map(int, input().split())) for _ in range(N)]

diff = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def tomato(ic):
    Q = deque()
    for i in ic:
        Q.append(i)
    day = -1
    while Q:
        for _ in range(len(Q)):
            t = Q.popleft()
            for (a, b) in diff:
                dx, dy = t[0] + a, t[1] + b
                if dx < 0 or dx == N or dy < 0 or dy == M:
                    continue

                if farm[dx][dy] == 0 and visit[dx][dy] == False:
                    Q.append([dx, dy])
                    farm[dx][dy] = 1
                    visit[dx][dy] = True
        day += 1
    for x in range(N):
        for y in range(M):
            if visit[x][y] == False:
                return  -1
            else:
                return day

ic = []
no = []
for x in range(N):
    for y in range(M):
        if farm[x][y] == 1:
            ic += [[x, y]]
        elif farm[x][y] == -1:
            no += [[x, y]]
visit = [[False] * M for _ in range(N)]
for a in range(len(ic)):
    visit[ic[a][0]][ic[a][1]] = True

for b in range(len(no)):
    visit[no[b][0]][no[b][1]] = True

print(tomato(ic))