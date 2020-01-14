def solution(A):
    A = str(A)
    result = ''
    cnt = 0
    for i in range(len(A)-1, -1, -1):
        print(i)
        if cnt != 3:
            cnt += 1
            result += A[i]
        elif A[i] == '-':
            result += A[i]
            break
        else:
            cnt = 0
            result += ','
            result += A[i]
            cnt += 1
    result = ''.join(reversed(result))
    return result



print(solution(-3456.78))