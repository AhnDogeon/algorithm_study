T = int(input())

for test_case in range(1, T + 1):
    line = list(map(int input().split()))
    total = 0
    for i in line:
        if i % 2:
            total += i
    print('#{} {}'.format(test_case, total))