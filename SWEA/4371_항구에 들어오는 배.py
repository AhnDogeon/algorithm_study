import sys
sys.stdin = open('4371_항구에 들어오는 배.txt', 'r')
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    line = []
    for n in range(N):
        line.append(int(input()))
    cnt = 0
    total = 1
    while line:
        if len(line) > 1:
            minus = line[1] - line[0]
            cnt += 1
        while True:
            total += minus
            if total in line:
                line.remove(total)
            else:
                if total > line[-1]:
                    total = 1
                    break
        if len(line) <= 1:
            break
    if cnt == 0:
        cnt += 1
    print('#{} {}'.format(test_case, cnt))
