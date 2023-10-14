# from collections import deque

# def bfs(x1, y1, x2, y2, maps):
#     queue = deque()
#     deque.append(x1, x2)

#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]

#     while queue:
#         x, y = queue.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]):
#                 continue
            

        

#     return  

# def solution():
#     N, M, steps = map(int, input().split())
    
#     for i in range(len(N)):
#         road = map(str, input())
    
#     x1, y1, x2, y2 = map(int, input().split())



#     return 


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프

print(array)