import sys
sys.stdin = open('전기버스2.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    arr.append(0)
    N = arr[0]

    oil = arr[1]
    cnt = 0
    i = 1
    while arr[i] != 0:
        tmp = i
        i = i + arr[i]
        for j in range(tmp + 1, i):
            if arr[j] - (i - tmp) > arr[i]:
                i = j
                cnt += 1
                break
        else:
            cnt += 1
    print(cnt)
