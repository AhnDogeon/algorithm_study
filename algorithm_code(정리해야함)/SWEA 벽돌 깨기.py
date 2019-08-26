import sys
from copy import deepcopy
from itertools import product
from time import time
sys.stdin = open('SWEA 벽돌 깨기.txt', 'r')

T = int(input())

def crush(a, b, gap): # a : 세로 좌표(H) b : 가로 좌표(W)
    board[a][b] = 0
    if gap == 0 or gap == 1:
        board[a][b] = 0
        return
    else:
        for i in range(1, gap):
            diff = [(i, 0), (-i, 0), (0, i), (0, -i)]
            for (x, y) in diff:
                dx, dy = a + x, b + y
                if 0 <= dx < H and 0 <= dy < W:
                    crush(dx, dy, board[dx][dy])

def down():
    for i in range(H-2, -1, -1):
        for j in range(W):
            if board[i][j] != 0 and board[i+1][j] == 0:
                cnt = 0
                for height in range(i+1, H):
                    if board[height][j] == 0:
                        cnt += 1
                board[i][j], board[i+cnt][j] = board[i+cnt][j], board[i][j]


for test_case in range(1, T + 1):
    a = time()
    N, W, H = map(int, input().split())
    real_board = []
    for _ in range(H):
        real_board.append(list(map(int, input().split())))

    lst = [i for i in range(W)]
    # print(lst)
    z = list(product(lst, repeat=N))
    # print(z)
    # for i in range(H):
    #     for j in range(W):
    #         print(real_board[i][j], end=' ')
    #     print()
    # print('==============================================================================================================================')

    minH = 0xffff

    for i in z: # 중복순열 안에서 도는 것
        board = deepcopy(real_board)
        for j in i: # (-1, -2, -3) 같이 돔
            for y in range(H):
                if board[y][j] != 0:
                    crush(y, j, board[y][j])# y : 세로 좌표(H), j : 가로 좌표(w), 그 지점의 값
                    down()
                    break
        result = 0
        for row in range(H):
            for col in range(W):
                if board[row][col] != 0:
                    result += 1
        if result < minH:
            minH = result
        #
        # for i in range(H):
        #     for j in range(W):
        #         print(board[i][j], end=' ')
        #     print()
        # print('-------------------------------------------------------------------------------------------------------------------------------')

    print('#{} {}'.format(test_case, minH))
    print(time() - a)