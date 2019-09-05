import sys
sys.stdin = open('17136_색종이 붙이기.txt', 'r')


board = [list(map(int, input().split())) for _ in range(10)]
visit = [[False] * 10 for _ in range(10)]

one_cnt = 0
for _ in range(10):
    for __ in range(10):
        if board[_][__] == 1:
            one_cnt += 1

paper_list = [5, 5, 5, 5, 5] # 0 : 5x5 1 : 4x4 2: 3X3 3: 2x2 4: 1x1


start_find = False
for i in range(10):
    for j in range(10):
        paper(i, j, paper_list)
        break
    if start_find == True: