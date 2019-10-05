import sys
sys.stdin = open('4.txt', 'r')

N = int(input())
arr = list(map(int, input().strip().split(' ')))

def DFS(x, arr):
    answer = 0
    for i in range(x+1, len(arr)):
        if arr[i] == 1:
            answer = i - x
            break

    for j in range(x - 1, 0, -1):
        if arr[j] == 1:
            if abs(j - x) < answer:
                answer = abs(j-x)
            break
    return answer

final = 0
for _ in range(len(arr)):
    if arr[_] == 0:
        result = DFS(_,arr)
        if result > final:
            final = result
print(final)