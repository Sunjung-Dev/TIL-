def solution(sizes):
    answer = 0

    width_list = list()
    length_list = list()

    
    for i in range(len(sizes)):
        width_list.append(sizes[i][0])
        length_list.append(sizes[i][1])
    
    #새로와 가로의 최대값을 먼저 구하기 
    width_list.sort(reverse=True)
    length_list.sort(reverse=True)

    width = width_list[0] #가로
    length = length_list[0] #세로 

    for i in range(1, len(sizes)):
        if width > length and length_list[i] > width:
            length = length_list[i]
        if length > width and width_list[i] > length:
            width = width_list[i]

    print(length, width)

    return answer

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))