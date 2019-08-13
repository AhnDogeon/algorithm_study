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

for yeon in k_list:
    minus_low = yeon[0] - yeon[2]
    minus_high = yeon[1] - yeon[2]
    plus_low = yeon[0] + yeon[2]
    plus_high = yeon[1] + yeon[2]

    # (minus_low, minus_high)
    # (plus_low, plus_high)

    gap_x = plus_low - minus_low
    gap_y = plus_high - minus_high

