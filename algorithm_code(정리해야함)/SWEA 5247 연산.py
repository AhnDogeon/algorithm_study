import sys
sys.stdin = open('SWEA 5247 연산.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [1, -1, 2, -10]
