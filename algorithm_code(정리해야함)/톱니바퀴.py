import sys
import collections
sys.stdin = open('톱니바퀴.txt', 'r')


gear_1 = collections.deque(list(map(int, input().split())))
gear_2 = collections.deque(list(map(int, input().split())))
gear_3 = collections.deque(list(map(int, input().split())))
gear_4 = collections.deque(list(map(int, input().split())))

lst = [0, gear_1, gear_2, gear_3, gear_4]


K = int(input())

for k in range(K):
    number, direction = map(int, input().split()) # number : 회전시킬 톱니바퀴 direction : 회전시킬 방향 (1 : 시계, -1 : 반시계)
    compare(lst[number], lst[number+1])