import sys
from copy import deepcopy
sys.stdin = open('2.txt', 'r')


T = int(input())
# 상(0), 하(1), 좌(2), 우(3)
for test_case in range(1, T+1):
    N = int(input())
    gap = []
    maxH = 0
    for n in range(N):
        gap.append(list(map(int, input().split())))
        if abs(gap[n][0]) >= maxH:
            maxH = abs(gap[n][0])
        if abs(gap[n][1]) >= maxH:
            maxH = abs(gap[n][1])
    total = 0
    while gap:
        for _ in range(len(gap)):
            if len(gap[_])>0:
                if gap[_][2] == 0:
                    gap[_][1] += 0.5
                elif gap[_][2] == 1:
                    gap[_][1] -= 0.5
                elif gap[_][2] == 2:
                    gap[_][0] -= 0.5
                elif gap[_][2] == 3:
                    gap[_][0] += 0.5
                if abs(gap[_][0]) > maxH or abs(gap[_][1]) > maxH:
                    gap[_] = []
        point_list = {}
        for a in range(len(gap)):
            if len(gap[a]) != 0:
                (x, y) = (gap[a][0], gap[a][1])
                if point_list.get((x, y)):
                    point_list[(x, y)].append(a)
                else:
                    point_list[(x,y)] = [a]
        for i in point_list:
            if len(point_list[i]) > 1:
                for j in point_list[i]:
                    total += gap[j][3]
                    gap[j] = []
        flag = 0
        for k in range(len(gap)):
            if len(gap[k]) == 0:
                flag += 1
        if flag == len(gap):
            print('#{} {}'.format(test_case, total))
            break
