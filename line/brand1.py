#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
def solution(roomNumber):
    count = 0
    # 딕셔너리 형태로 한 세트
    number_dic = {'1' : 1, '2': 1, '3': 1, '4':1, '5':1, '6':1, '7':1, '8':1, '9':1, '0':1}
    for i in str(roomNumber):
        if i == '9':
            if number_dic[i] >= 1:
                number_dic[i] -= 1
            elif number_dic['6'] >= 1:
                number_dic['6'] -=1
            else:
                count += 1
                for j in number_dic:
                    number_dic[j] += 1
                number_dic[i] -= 1
        elif i == '6':
            if number_dic[i] >= 1:
                number_dic[i] -= 1
            elif number_dic['9'] >= 1:
                number_dic['9'] -=1
            else:
                count += 1
                for j in number_dic:
                    number_dic[j] += 1
                number_dic[i] -= 1
        elif number_dic[i] >= 1:
            number_dic[i] -= 1
        else:
            count += 1
            for j in number_dic:
                    number_dic[j] += 1
            number_dic[i] -= 1
    return count

solution(122)