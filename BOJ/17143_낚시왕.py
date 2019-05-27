import sys
import copy
sys.stdin = open('17143_낚시왕.txt', 'r')
# 동, 서, 남, 북 방향 좌표 정하기부터 시작입니다. v 부터

R, C, M = map(int, input().split())

catch = 0

board = []
for i in range(R):
    line = []
    for j in range(C):
        info = [0, 0, 0]
        line.append(info)
    board.append(line)

if M:
    for setting in range(M):
        r, c, s, d, z = map(int, input().split())
        board[r-1][c-1][0] = s
        board[r-1][c-1][1] = d
        board[r-1][c-1][2] = z
else:
    print(0)


# 디버깅-----------------
for a in range(R):
    for b in range(C):
        print(board[a][b], end=' ')
    print()
# 디버깅-----------------

def catch(x):
    global catch
    for y in range(R):
        if board[x][y][2]:
            catch += 1
            board[x][y] = [0, 0, 0]
        break

def move(board, copy_board):
    for i in range(R):
        for j in range(C):
            if board[i][j][2]:
                current_i = i
                current_j = j
                if board[i][j][1] == 1:
                    v = board[i][j][0] # 몇 칸 이동해야하는지
                    while v:
                        if v - current_j >= 0:
                            v = v - current_j
                            current_j = 0
                            if v == 0:
                                break
                        else:
                            current_j = current_j - v
                            v = 0
                            break
                        if v - current_j >= 0:
                            v = v - current_j
                            current_j = R - 1
                            if v == 0:
                                break
                        else:
                            current_j = v
                            break
                elif board[i][j][1] == 2:
                    v = board[i][j][0] # 몇 칸 이동해야하는지
                    while v:
                        if v - (R - 1 - current_j) >= 0:
                            v = v - (R - 1 - current_j)
                            current_j = R - 1
                            if v == 0:
                                break
                        else:
                            current_j = current_j + v
                            v = 0
                            break
                        if v - current_j >= 0:
                            v = v - current_j
                            current_j = R - 1
                            if v == 0:
                                break
                        else:
                            current_j = v
                            break
                elif board[i][j][1] == 3:
                    v = board[i][j][0] # 몇 칸 이동해야하는지
                    while v:
                        if v - current_j >= 0:
                            v = v - current_j
                            current_j = 0
                            if v == 0:
                                break
                        else:
                            current_j = current_j - v
                            v = 0
                            break
                        if v - current_j >= 0:
                            v = v - current_j
                            current_j = R - 1
                            if v == 0:
                                break
                        else:
                            current_j = v
                            break
                elif board[i][j][1] == 4:
                    v = board[i][j][0] # 몇 칸 이동해야하는지
                    while v:
                        if v - current_j >= 0:
                            v = v - current_j
                            current_j = 0
                            if v == 0:
                                break
                        else:
                            current_j = current_j - v
                            v = 0
                            break
                        if v - current_j >= 0:
                            v = v - current_j
                            current_j = R - 1
                            if v == 0:
                                break
                        else:
                            current_j = v
                            break


for x in range(C):
    catch(x) # 잡는함수()
    copy_board = []
    for i in range(R):
        line = []
        for j in range(C):
            info = [0, 0, 0]
            line.append(info)
        copy_board.append(line)
    move(board, copy_board) # 상어이동함수()
    board = copy.deepcopy(copy_board)