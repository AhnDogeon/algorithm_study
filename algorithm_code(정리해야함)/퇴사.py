import sys
import copy
sys.stdin = open('퇴사.txt', 'r')

def DG(v, result):
    # result = [v]
    global maxH
    isone = False
    arr = []
    for i in range(v[0] + 1, len(board) - 1):
        if board[i][0] > v[2] and board[i][2] <= N:
            arr.append(board[i])
    if len(arr) == 0:
        isone = True # 첫 번째 인자부터 범위초과해서 하나만 들어올 경우 혹은 그 뒤에 두 개 째 들어오는 경우
        arr.append(v)
    for j in range(len(arr)):
        tmp_result = copy.deepcopy(result)
        if isone == False: # 하나만 들어오는게 아닐 때 모두
            tmp_result.append(arr[j])
        cnt = 0
        for x in tmp_result:
            cnt += x[1]
        if cnt > maxH:
            maxH = cnt
        if isone == False: # 하나만 들어오는게 아닐 때 모두
            DG(arr[j], tmp_result)
    return maxH


N = int(input())

board = [[0, 0]]

for _ in range(N):
    board.append(list(map(int, input().split())))

for i in range(1, len(board)):
    board[i].append(i + board[i][0] - 1)
    board[i][0] = i
board.append([16,0,16])

maxH = 0
final_result = 0
result = []
for i in range(1, N + 1):
    if board[i][2] < N + 1:
        result = [board[i]]
        final_result = DG(board[i], result)

print(final_result)