from itertools import combinations
cnt = 0
def maxInversions(prices):
    def comb_r(k, s):
        global cnt
        if k == R:
            total = 5001
            isArr = False
            for i in result:
                if total > i:
                    total = i
                    isArr = True
                else:
                    isArr = False
                    break
            if isArr == True:
                cnt += 1
        else:
            for i in range(s, N + k - R + 1):
                result[k] = prices[i]
                if k == 0:
                    comb_r(k + 1, i + 1)
                else:
                    if result[k] < result[k - 1]:
                        comb_r(k + 1, i + 1)

    N = len(prices)
    R = 3
    result = [0] * R
    if N >= 3:
        comb_r(0, 0)
    return cnt

print(maxInversions([5,10,7,4,5,11]))

