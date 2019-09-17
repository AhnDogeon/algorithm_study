a = [0, 5, 6, 7]

N = 4

R = 3

def per(k): # 순열
    if k == R:
        print(t)
    else:
        for i in range(N):
            if visit[i]:
                continue
            visit[i] = True
            t[k] = a[i]
            per(k+1)
            visit[i] = False

visit = [False] * N
t = [0] * R
per(0)


