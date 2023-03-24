def solution(lottos, win_nums):
    answer = []
    same_num = 0
    zero_num = 0

    
    
    for i in range(6):
        if lottos[i] == 0:
            zero_num += 1
        if lottos[i] in win_nums: 
            same_num += 1

    if same_num == 6:
        answer.append(1, 1)
    if zero_num == 6 and same_num == 0:
        answer.append(1, 6)
    else:
        answer.append()
    return answer

solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35])