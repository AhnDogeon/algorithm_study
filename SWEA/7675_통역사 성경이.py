import sys
sys.stdin = open('7675_통역사 성경이.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = str(input())
    result = arr.split(" ")
    print(arr)
    print(result)