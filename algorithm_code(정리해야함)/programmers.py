Keyboard = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['*', '0', '#']]
# CurPos 는 [x, y], target은 string
diff = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def Left(Cur_pos, target):
    Keyboard_Dis = [[0, 0, 0] for _ in range(4)]
    Keyboard_visit = [[False, False, False] for _ in range(4)]
    Keyboard_visit[Cur_pos[0]][Cur_pos[1]] = True

    Que = [Cur_pos]
    while Que:
        v = Que.pop(0)
        for x, y in diff:
            dx = v[0] + x
            dy = v[1] + y
            if 0 <= dx < 4 and 0 <= dy < 3:
                if Keyboard_visit[dx][dy] == False:
                    Keyboard_visit[dx][dy] = True
                    Keyboard_Dis[dx][dy] = Keyboard_Dis[v[0]][v[1]] + 1
                    Que.append([dx, dy])
                if Keyboard[dx][dy] == str(target):
                    return [dx, dy], Keyboard_Dis[dx][dy]


def Right(Cur_pos, target):
    Keyboard_Dis = [[0, 0, 0] for _ in range(4)]
    Keyboard_visit = [[False, False, False] for _ in range(4)]
    Keyboard_visit[Cur_pos[0]][Cur_pos[1]] = True

    Que = [Cur_pos]
    while Que:
        v = Que.pop(0)
        for x, y in diff:
            dx = v[0] + x
            dy = v[1] + y
            if 0 <= dx < 4 and 0 <= dy < 3:
                if Keyboard_visit[dx][dy] == False:
                    Keyboard_visit[dx][dy] = True
                    Keyboard_Dis[dx][dy] = Keyboard_Dis[v[0]][v[1]] + 1
                    Que.append([dx, dy])
                if Keyboard[dx][dy] == str(target):
                    return [dx, dy], Keyboard_Dis[dx][dy]



def solution(numbers, hand):
    answer = ''
    arr_left = [1, 4, 7]
    arr_right = [3, 6, 9]
    leftPos = [3, 0]
    rightPos = [3, 2]

    for i in numbers:
        if i in arr_left:
            answer += 'L'
            for a in range(len(Keyboard)):
                for b in range(len(Keyboard[a])):
                    if str(i) == Keyboard[a][b]:
                        leftPos = [a, b]
                        break
        elif i in arr_right:
            answer += 'R'
            for a in range(len(Keyboard)):
                for b in range(len(Keyboard[a])):
                    if str(i) == Keyboard[a][b]:
                        rightPos = [a, b]
                        break
        else:
            tmp_leftPos, left_Dis = Left(leftPos, i)
            tmp_rightPos, right_Dis = Right(rightPos, i)
            if left_Dis < right_Dis:
                answer += 'L'
                leftPos = tmp_leftPos
            elif right_Dis < left_Dis:
                answer += 'R'
                rightPos = tmp_rightPos
            elif left_Dis == right_Dis:
                if hand == 'right':
                    answer += 'R'
                    rightPos = tmp_rightPos
                elif hand == 'left':
                    answer += 'L'
                    leftPos = tmp_leftPos
    print(answer)
    return answer

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right')