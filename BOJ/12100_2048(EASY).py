import sys
from copy import deepcopy
sys.stdin = open('12100_2048(EASY).txt', 'r')

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]


def up(up_board):
    for i in range(1, N):
        for j in range(N):
            if up_board[i][j]:
                cnt = 0
                for a in range(i - 1, -1, -1):
                    if up_board[a][j] == 0:
                        cnt += 1
                up_board[i-cnt][j] = up_board[i][j]
                if cnt > 0:
                    up_board[i][j] = 0

    for i in range(1, N):
        for j in range(N):
            if up_board[i][j] == up_board[i-1][j]:
                up_board[i-1][j] += up_board[i][j]
                up_board[i][j] = 0

    for i in range(1, N):
        for j in range(N):
            if up_board[i][j]:
                cnt = 0
                for a in range(i - 1, -1, -1):
                    if up_board[a][j] == 0:
                        cnt += 1
                up_board[i-cnt][j] = up_board[i][j]
                if cnt > 0:
                    up_board[i][j] = 0
    return up_board

def down(down_board):
    for i in range(N-2, -1, -1):
        for j in range(N):
            if down_board[i][j]:
                cnt = 0
                for a in range(i + 1, N):
                    if down_board[a][j] == 0:
                        cnt += 1
                down_board[i+cnt][j] = down_board[i][j]
                if cnt > 0:
                    down_board[i][j] = 0

    for i in range(N-1, 0, -1):
        for j in range(N):
            if down_board[i][j] == down_board[i-1][j]:
                down_board[i][j] += down_board[i-1][j]
                down_board[i-1][j] = 0

    for i in range(N - 2, -1, -1):
        for j in range(N):
            if down_board[i][j]:
                cnt = 0
                for a in range(i + 1, N):
                    if down_board[a][j] == 0:
                        cnt += 1
                down_board[i + cnt][j] = down_board[i][j]
                if cnt > 0:
                    down_board[i][j] = 0
    return down_board

def left(left_board):
    for i in range(N):
        for j in range(1, N):
            if left_board[i][j]:
                cnt = 0
                for a in range(j - 1, -1, -1):
                    if left_board[i][a] == 0:
                        cnt += 1
                left_board[i][j-cnt] = left_board[i][j]
                if cnt > 0:
                    left_board[i][j] = 0

    for i in range(N):
        for j in range(1, N):
            if left_board[i][j] == left_board[i][j-1]:
                left_board[i][j-1] += left_board[i][j]
                left_board[i][j] = 0

    for i in range(N):
        for j in range(1, N):
            if left_board[i][j]:
                cnt = 0
                for a in range(j - 1, -1, -1):
                    if left_board[i][a] == 0:
                        cnt += 1
                left_board[i][j - cnt] = left_board[i][j]
                if cnt > 0:
                    left_board[i][j] = 0
    return left_board

def right(right_board):
    for i in range(N):
        for j in range(N - 2, -1, -1):
            if right_board[i][j]:
                cnt = 0
                for a in range(i + 1, N):
                    if right_board[i][a] == 0:
                        cnt += 1
                right_board[i][j + cnt] = right_board[i][j]
                if cnt > 0:
                    right_board[i][j] = 0

    for i in range(N):
        for j in range(N - 1, 0, -1):
            if right_board[i][j] == right_board[i][j - 1]:
                right_board[i][j] += right_board[i][j - 1]
                right_board[i][j - 1] = 0

    for i in range(N):
        for j in range(N - 2, -1, -1):
            if right_board[i][j]:
                cnt = 0
                for a in range(i + 1, N):
                    if right_board[i][a] == 0:
                        cnt += 1
                right_board[i][j + cnt] = right_board[i][j]
                if cnt > 0:
                    right_board[i][j] = 0
    return right_board

cnt = 0

def game(board, cnt):
    if cnt < 5:
        up_board = deepcopy(board)
        up_board = up(up_board)
        game(up_board, cnt+1)

        down_board = deepcopy(board)
        down_board = down(down_board)
        game(down_board, cnt + 1)

        right_board = deepcopy(board)
        right_board = right(right_board)
        game(right_board, cnt + 1)

        left_board = deepcopy(board)
        left_board = left(left_board)
        game(left_board, cnt + 1)

        if cnt == 5:
            # up down right left 돌면서 최댓값 찾기
            MAX = 0
            for up_i in range(N):
                for up_j in range(N):
                    if up_board[up_i][up_j] >= MAX:
                        MAX = up_board[up_i][up_j]

            for down_i in range(N):
                for down_j in range(N):
                    if down_board[down_i][down_j] >= MAX:
                        MAX = down_board[down_i][down_j]

            for left_i in range(N):
                for left_j in range(N):
                    if left_board[left_i][left_j] >= MAX:
                        MAX = left_board[left_i][left_j]

            for right_i in range(N):
                for right_j in range(N):
                    if right_board[right_i][right_j] >= MAX:
                        MAX = right_board[right_i][right_j]
            return MAX

res = game(board, cnt)
print(res)