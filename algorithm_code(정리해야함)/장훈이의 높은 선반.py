import sys
import itertools
sys.stdin = open('장훈이의 높은 선반.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    result = []
    for i in range(N, -1, -1):
        z = list(itertools.combinations(arr, i))
        for j in z:
            if sum(j) < B:
                pass
            else:
                result.append(sum(j))
    print('#{} {}'.format(test_case, min(result) - B))