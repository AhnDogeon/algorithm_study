import sys
from copy import deepcopy
sys.stdin = open('input_17143.txt', 'r')

R, C, M = map(int, input().split())

lst = [[[-1, -1, -1] for _in range(C)] for _ in range(R)]
cp_lst = [[[-1, -1, -1] for _in range(C)] for _ in range(R)]
for _ in range(M):
   r, c, s, d, z = map(int, input().split())
   lst[r-1][c-1] = [s, d, z]

for o in range(R):
   print(lst[o])


result = 0
cnt = 0

while cnt < C:
   # 낚시꾼 발 밑을 돌면서
   for i in range(R):
       # 상어가 있으면
       if lst[i][cnt][0] != -1:
           # 상어 크기 더하고
           result += lst[i][cnt][2]

           # 상어 없애주고
           lst[i][cnt][0] = -1
           lst[i][cnt][1] = -1
           lst[i][cnt][2] = -1
           break
   cnt += 1

   # 상어 이동

   for a in range(R):
       for b in range(C):
           # 상어가 있을 때
           if lst[a][b][0] != -1:

               # 방향이 아래일 때
               if lst[a][b][1] == 2:
                   dir = lst[a][b][1]
                   long = lst[a][b][0]
                   while long > 0:
                       # 속력 < 내가 갈 수 있는 칸
                       if long < R - a - 1:
                           long = 0
                           my_index = a + lst[a][b][2]

                           # cp 에 상어가 없다면
                           if cp_lst[my_index][b][0] == -1:
                               cp_lst[my_index][b][0] = lst[a][b][0]
                               cp_lst[my_index][b][1] = dir
                               cp_lst[my_index][b][2] = lst[a][b][2]

                               lst[a][b][0] = -1
                               lst[a][b][1] = -1
                               lst[a][b][2] = -1

                           # cp 에 상어가 있다면
                           else:
                               if lst[a][b][2] > cp_lst[my_index][b][2]:
                                   cp_lst[my_index][b][0] = lst[a][b][0]
                                   cp_lst[my_index][b][1] = dir
                                   cp_lst[my_index][b][2] = lst[a][b][2]

                                   lst[a][b][0] = -1
                                   lst[a][b][1] = -1
                                   lst[a][b][2] = -1

                               else:
                                   lst[a][b][0] = -1
                                   lst[a][b][1] = -1
                                   lst[a][b][2] = -1

                       # 속력 >= 내가 갈 수 있는 칸
                       else:
                           if dir == 2:
                               my_index = R - 1
                               long = lst[a][b][2] - (R - 1)
                               dir = 1

                           elif dir == 1:
                               my_index =


               # cp_lst 에 상어가 있다면

               # cp_lst 에 상어가 없다면