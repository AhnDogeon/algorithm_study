def perm_r(k):
    if k == R :
        print(t)
    else:
        for i in range(N):
            if visited[i]:
                continue
            t[k] = i + 1
            visited[i] = 1
            perm_r(k + 1)
            visited[i] = 0

N = 8
R = 8
a = [0,1,2,4,5,6,7,8]
t = [0] * R

# t = [0] * N
visited = [0] * N
perm_r(0)