import sys
sys.stdin = open('15686_스타트와링크.txt', 'r')

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

people = [_ for _ in range(1, N + 1)]

R = int(N / 2)
t = [0] * R


perm_list = []
def comb(k, s):
    if k == R:
        tt = []
        nott = []
        for a in people:
            if a not in t:
                nott.append(a)
            else:
               tt.append(a)
        perm_list.append([tt, nott])
    else:
        for i in range(s, N + (k - R) + 1):
            t[k] = people[i]
            comb(k+1, i+1)


comb(0, 0)



print(perm_list)

def perm(team_list, gap):
    if gap == 2:
        pass

    else:
        for c_i in range(R):
            if visit[c_i]:
                continue



for arr in perm_list:
    visit = [False] * R
    total_a = 0
    total_b = 0
    perm(arr[0], 0)
    perm(arr[1], 0)