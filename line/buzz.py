before_list = ['(', '{', '[']
after_list = [')', '}', ']']
def braces(values):
    final = []
    for j in range(len(values)):
        arr = values[j]
        answer = 'YES'
        result = []
        for i in range(len(arr)):
            # 닫는 괄호 일 때
            if arr[i] in after_list:
                if result:
                    idx = after_list.index(arr[i])
                    if idx == 0:
                        if result[-1] == '(':
                            result.pop()
                        else:
                            answer = 'NO'
                            break
                    elif idx == 1:
                        if result[-1] == '{':
                            result.pop()
                        else:
                            answer = 'NO'
                            break
                    elif idx == 2:
                        if result[-1] == '[':
                            result.pop()
                        else:
                            answer = 'NO'
                            break
                else:
                    answer = 'NO'
                    break
            else:
                result.append(arr[i])
        final.append(answer)
    return final

print(braces(['{[()]}', '{[(])}','{{[[(())]]}}']))


