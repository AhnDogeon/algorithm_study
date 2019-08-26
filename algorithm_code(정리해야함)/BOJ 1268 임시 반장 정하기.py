import sys
sys.stdin = open('BOJ 1268 임시 반장 정하기.txt', 'r')

N = int(input())

ban = [list(map(int, input().split())) for _ in range(N)]


dp = [0 for _ in range(N)]

for i in range(N):
    result = []
    for j in range(5):
        for k in range(N):
            if k != i:
                if ban[i][j] == ban[k][j] and k not in result:
                    result.append(k)
    dp[i] = len(result)
print(dp.index(max(dp)) + 1)

