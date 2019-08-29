import sys
sys.stdin = open('2.txt', 'r')

T = int(input())
# 상(0), 하(1), 좌(2), 우(3)
for test_case in range(1):
    N = int(input())
    gap = []
    maxX = 0
    maxY = 0
    for n in range(N):
        gap.append(list(map(int, input().split())))
        if abs(gap[n][0]) >= maxX:
            maxX = abs(gap[n][0])
        if abs(gap[n][1]) >= maxY:
            maxY = abs(gap[n][1])

    board = [[[] for _ in range(2 * maxX + 2)] for _ in range(2 * maxY + 2)]
    for m in range(len(gap)):
        gap[m][0] += maxX
        gap[m][1] += maxY
    print(len(board))
    print(len(board[0]))
    total = 0

    while gap:
        musi_list = []
        for _ in range(len(gap)):
            if gap[_][2] == 0:
                gap[_][1] += 1
            elif gap[_][2] == 1:
                gap[_][1] -= 1
            elif gap[_][2] == 2:
                gap[_][0] -= 1
            elif gap[_][2] == 3:
                gap[_][0] += 1
            if gap[_][0] < 0 or gap[_][0] > maxX + 1 or gap[_][1] < 0 or gap[_][1] > maxY + 1:
                musi_list.append(gap[_])
        for _ in range(len(musi_list)):
            gap.remove(musi_list[_])

        result = []
        for a in range(len(gap)):
            if board[gap[a][0]][gap[a][1]]:
                if gap[a] not in board[gap[a][0]][gap[a][1]]:
                    if [[gap[a][0], gap[a][1]]] not in result:
                        result.append([gap[a][0], gap[a][1]])
                        total += gap[a][3]
            else:
                board[gap[a][0]][gap[a][1]] = gap[a]
        print(result)


    #
    #
    #     print('======================')
    #     result = []
    #     for a in range(len(gap)):
    #         for b in range(a+1, len(gap)):
    #             if gap[b][0] == gap[a][0] and gap[b][1] == gap[a][1]:
    #                     if gap[a] not in result:
    #                         result.append(gap[a])
    #                         total += gap[a][3]
    #                     if gap[b] not in result:
    #                         result.append(gap[b])
    #                         total += gap[b][3]
    #     while result:
    #         gap.remove(result.pop())
    #     if len(gap) == 0:
    #         break
    #     maxH = 0
    #     for x in range(len(gap)):
    #         if abs(gap[x][0]) >= maxH:
    #             maxH = abs(gap[x][0])
    #         if abs(gap[x][1]) >= maxH:
    #             maxH = abs(gap[x][1])
    #     board = [[[] for _ in range(2 * maxH)] for _ in range(2 * maxH)]
    # print('#{} {}'.format(test_case, total))
