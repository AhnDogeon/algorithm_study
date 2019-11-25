def perfectSubstring(s, k):
    # Write your code here
    cnt = 0
    for i in range(k, len(s)):
        for j in range(len(s) - k):
            arr = s[j:j+k]
            for k in arr:
                if arr.count(k) == k:
                    pass
                else:
                    break
            else:
                cnt += 1
    return cnt

perfectSubstring('1102021222', 2)