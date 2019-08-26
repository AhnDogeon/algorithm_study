import sys
sys.stdin = open('1018 체스판 다시 칠하기.txt', 'r')


def WB(arr):
    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i % 2 == 0:
                if j % 2 == 0:
                    if arr[i][j] != 'W':
                        cnt += 1
                else:
                    if arr[i][j] != 'B':
                        cnt += 1
            else:
                if j % 2 == 0:
                    if arr[i][j] != 'B':
                        cnt += 1
                else:
                    if arr[i][j] != 'W':
                        cnt += 1
    return cnt


def BW(arr):
    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i % 2 == 0:
                if j % 2 == 0:
                    if arr[i][j] != 'B':
                        cnt += 1
                else:
                    if arr[i][j] != 'W':
                        cnt += 1
            else:
                if j % 2 == 0:
                    if arr[i][j] != 'W':
                        cnt += 1
                else:
                    if arr[i][j] != 'B':
                        cnt += 1
    return cnt


N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(input()))

# print(board)

cnt_list = []
for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        result = []
        for k in range(8):
            result.append(board[i+k][j:j+8])
        # print(result)
        y = WB(result)
        z = BW(result)
        cnt_list.append(min(y, z))

print(min(cnt_list))