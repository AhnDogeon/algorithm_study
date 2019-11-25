# print(sum(done_dict.values()))
def programmerStrings(s):
    count_dict = {'p': 1, 'r': 3, 'o': 1, 'g': 1, 'a': 1, 'm': 2, 'e': 1}
    done_dict = {'p': 1, 'r': 3, 'o': 1, 'g': 1, 'a': 1, 'm': 2, 'e': 1}
    cnt = 0
    # Write your code here
    cnt_bool = False
    for i in s:
        if sum(count_dict.values()) == 0:
            cnt_bool = True
            count_dict = {'p': 1, 'r': 3, 'o': 1, 'g': 1, 'a': 1, 'm': 2, 'e': 1}
        if i in done_dict and done_dict[i] and cnt_bool == False:
            cnt_bool = False
            count_dict[i] -= 1
        elif cnt_bool == True and count_dict == done_dict:
            cnt += 1

    return cnt

print(programmerStrings('progxrammerrxproxgrammer'))