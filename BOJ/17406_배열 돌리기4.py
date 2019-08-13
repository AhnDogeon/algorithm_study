import sys

sys.stdin = open('17406_배열 돌리기4.txt', 'r')

N, M, K = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

print(board)

k_list = []
for _ in range(K):
    k_list.append(list(map(int, input().split())))

print(k_list)

def dol(start, end):
    global board
    if start == end:
        return
    else:
        tmp2 = -1
        x = start[0]
        y = start[1]
        while True:
            if y != end[1]:
                tmp = board[x][y + 1]
                y += 1
                board[x][y] = tmp
            else:
                break
        while True:
            if x != end[0]:
                tmp = board[x][y]
                y += 1
                board[x][y] = tmp
            else:



        start = [start[0] + 1, start[1] + 1]
        end = [end[0] - 1, end[1] - 1]
        dol(start, end)




for yeon in k_list:
    minus_low = yeon[0] - yeon[2]
    minus_high = yeon[1] - yeon[2]
    plus_low = yeon[0] + yeon[2]
    plus_high = yeon[1] + yeon[2]

    start = [minus_low, minus_high]
    end = [plus_low, plus_high]

    dol(start, end)


