import sys
sys.stdin = open('BOJ_2573_빙산.txt', 'r')

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
visit = [[False for _ in range(M)] for _ in range(N)]

print(visit)

while True:
    for x in range(N):
        for y in range(M):
            if 
