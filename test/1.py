import sys
sys.stdin = open('1.txt', 'r')

T = int(input())

success = False
def shuffle(Left, Right, time):
    global time_list, success
    if time > 5:
        return
    for x in range(N):
        L_index = 0
        R_index = 0
        result = []
        if x < N/2:
            for y in range(N):
                if int(N/2) - y > x:
                    L_index += 1
                    result.append('L')
                else:
                    if R_index < N/2:
                        R_index += 1
                        result.append('R')
                    if L_index < N/2:
                        L_index += 1
                        result.append('L')
            L_idx = 0
            R_idx = 0
            final_result = []
            for k in result:
                if k == 'L':
                    final_result.append(Left[L_idx])
                    L_idx += 1
                elif k == 'R':
                    final_result.append(Right[R_idx])
                    R_idx += 1
            if final_result == sortCard or final_result == reversesortCard:
                success = True
                time_list.append(time)
                return
            else:
                shuffle(Left, Right, time+1)
        else:
            for y in range(N):
                if x - int(N/2) >= y:
                    R_index += 1
                    result.append('R')
                else:
                    if L_index < N/2:
                        L_index += 1
                        result.append('L')
                    if R_index < N/2:
                        R_index += 1
                        result.append('R')
            L_idx = 0
            R_idx = 0
            final_result = []
            for k in result:
                if k == 'L':
                    final_result.append(Left[L_idx])
                    L_idx += 1
                elif k == 'R':
                    final_result.append(Right[R_idx])
                    R_idx += 1
            if final_result == sortCard or final_result == reversesortCard:
                success = True
                time_list.append(time)
                return
            else:
                shuffle(Left, Right, time + 1)




for test_case in range(1, T+1):
    N = int(input())
    card = list(map(int, input().split()))
    card_L = card[0:int(len(card)/2)]
    card_R = card[int(len(card)/2):]

    sortCard = sorted(card)
    reversesortCard = list(reversed(sortCard))
    time_list = []
    time = 0
    shuffle(card_L, card_R, time)
    if fail:
        print(-1)
    else:
        print(time_list)