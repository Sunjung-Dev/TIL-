from itertools import permutations


def solution(numbers):
    answer = ''
    max_num = 0

    str_list = list()
    for i in range(len(numbers)):
        str_list.append(str(numbers[i]))
    
    for num in list(permutations(str_list, len(str_list))):
        num = ''.join(num)
        if int(num) > max_num:
            max_num = int(num)
    
    answer = str(max_num)
    return answer

print(solution([3, 30, 34, 5, 9]))