import sys
sys.stdin = open('2차원배열의합.txt', 'r')

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]


K = int(input())

for test_case in range(K):
    i, j, x, y = map(int, input().split())
    result = 0
    for a in range(i - 1, x):
        for b in range(j - 1, y):
            result += board[a][b]
    print(result)