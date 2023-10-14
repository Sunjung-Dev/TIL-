import sys
from collections import deque

def main():
    message = list(input()) #HELLOWORLD
    key = str(input())

    key_box = list()
    alphabet_list = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    temp = [] 
    key_box_list = []
    for i in range(len(key)):
        if key[i] not in key_box:
            key_box.append(key[i])
            if len(temp) == 5:
                key_box_list.append(temp)
                temp = []
            temp.append(key[i])
    
    for i in range(len(alphabet_list)):
        if alphabet_list[i] not in key_box:
            key_box.append(alphabet_list[i])
            if len(temp) == 5:
                key_box_list.append(temp)
                temp = []
            temp.append(alphabet_list[i])
    
    key_box_list.append(temp)

    # 'XXYYY'
    # XQ XY YX YX 
    # xx yy yx xx 
    # xq xy yq xq yx xq xx
    for i in range(0, len(message), 2):
        if message[i] == 'X' and message[i+1] == 'X':
            message.insert(i+1, 'Q')
        elif message[i] == message[i+1]:
            message.insert(i+1, 'X')
        print(message)
    if len(message) % 2 == 1: 
        message.append('X')

    new_message = ''
    message_list = []
    for i in range(0, len(message), 2):
        temp = message[i:i+2]
        message_list.append(temp)

    # 1. 같은행에 있을 경우 오른쪽 한칸 이동 
    # 2. 같은 열에 있을 경우 아래쪽으로 한칸 이동 
    # 3. 열 서로 교환 

    for i in range(len(message_list)):
        first_x = 0
        first_y = 0
        second_x = 0
        second_y = 0

        for j in range(len(key_box_list)):
            if message_list[i][0] in key_box_list[j]:
                first_x = j
                first_y = key_box_list[j].index(message_list[i][0])
            if message_list[i][1] in key_box_list[j]:
                second_x = j
                second_y = key_box_list[j].index(message_list[i][1])

        if first_x == second_x:
            if first_y + 1 > 4:
                first_y = -1
            if second_y + 1 > 4:
                second_y = -1
            new_message += (key_box_list[first_x][first_y+1] + key_box_list[second_x][second_y+1])
        
        elif first_y == second_y:
            if first_x + 1 > 4:
                first_x = -1
            if second_x + 1 > 4:
                second_x = -1
            new_message += key_box_list[first_x+1][first_y] + key_box_list[second_x+1][second_y]

        else:
            new_message += key_box_list[first_x][second_y] + key_box_list[second_x][first_y]
            
    return new_message

print(main())
            

            