import sys
sys.stdin = open('17136_색종이 붙이기.txt', 'r')

board = [list(map(int, input().split())) for _ in range(10)]

paper = [0, 5, 5, 5, 5, 5]

answer = -1
count_one = sum(sum(m) for m in board)
print(count_one)

def DFS(result):



DFS(0)
