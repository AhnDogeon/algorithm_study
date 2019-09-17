import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
zero_nine = {
    "ZRO": 0,
    "ONE": 1,
    "TWO": 2,
    "THR": 3,
    "FOR": 4,
    "FIV": 5,
    "SIX": 6,
    "SVN": 7,
    "EGT": 8,
    "NIN": 9
}

for test_case in range(1, T+1):
    number, N = map(str, input().split())
    line = int(N)
    word = list(map(str, input().split()))
    new_list = []
    for i in word:
        new_list.append(zero_nine[i])

    for x in range(line-1, 0, -1):
        for y in range(0, x):
            if new_list[y] > new_list[y+1]:
                new_list[y], new_list[y+1] = new_list[y+1], new_list[y]

    print(f'{number}')
    for a in new_list:
        for name, b in zero_nine.items():
            if a == b:
                print(f'{name}' end=" ")
    print()