import sys
sys.stdin = open('로봇청소기.txt', 'r')
N, M = map(int, input().split())

r, c, d = map(int, input().split())


arr = [[0, -1], [1, 0], [0, 1], [-1, 0]]
current_list = [0, 3, 2, 1]
def rec(a, b, c, board):
    board[a][b] = 2
    while True:
        x = a
        y = b
        current = current_list.index(c)
        for i in range(4):
            x = a + arr[current][0]
            y = b + arr[current][1]
            current += 1
            current = current % 4
            if board[x][y] == 0:
                a = x
                b = y
                c = current_list[current]
                board[a][b] = 2
                break
            else:
                continue
        else:
            c = current_list[current]
            current += 1
            current = current % 4
            a = a + arr[current][0]
            b = b + arr[current][1]
            if board[a][b] != 1:
                pass
            else:
                break
    return board




board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

rec(r, c, d, board)

result = 0
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == 2:
            result += 1
print(result)