N = ['a', 'b', 'c']
R = 3

selected = [[] for _ in range(R)]
print(selected)
def full(depth):
    if R == depth:
        for i in range(R):
            print(selected[i], end=' ')
        print()
        return

    for j in N:
        selected[depth] = j
        full(depth+1)


full(0)