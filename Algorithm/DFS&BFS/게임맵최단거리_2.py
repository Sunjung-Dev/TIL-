from collections import deque

def bfs(x, y, maps):
    # 상, 하, 좌, 우 
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))

    while(queue):

        #queue이기 때문에 왼쪽부터 뽑을 것임 (선입선출)
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 1 or ny < 1 or nx > len(maps) or ny > len(maps[0]):
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                # 바로 직전의 좌표 + 1
                maps[nx][ny] = maps[x][y] + 1
                # queue에 append 해주는 이유는 방금 그 좌표를 기준으로 다음 좌표를 봐야하기 때문에 
                queue.append((nx, ny))

    if maps[-1][-1] == 1:
        return -1

    # 마지막 좌표의 값을 return 해줄 것 
    return maps[-1][-1]


def solution(maps):
    answer = 0
    answer = bfs(1, 1, maps)
    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))




#일권님 

#up, Down, Left, Right
# def solution(maps):
#     maps = np.array(maps)
#     maps2 = np.pad(maps, ((1,1),(1,1)), 'constant', constant_values=0)
#     visited = set()
#     maps2[1,1]=0
#     queue = deque([(1,1,0)])
#     while queue:
#         m, n, result = queue.popleft()
#         if (m, n) == (maps.shape[0], maps.shape[1]):
#             return result + 1  # add 1 to account for starting position
#         for (i, j) in [(m-1,n), (m+1,n), (m,n-1), (m,n+1)]:  #up, Down, Left, Right
#             if (i,j) not in visited and maps2[i,j] == 1:
#                 visited.add((i,j))
#                 queue.append((i, j, result+1))
#         # print(queue)
#     return -1  # destination not reachable

# deque([(2, 1, 1)])
# deque([(3, 1, 2)])
# deque([(4, 1, 3)])
# deque([(4, 2, 4)])
# deque([(4, 3, 5)])
# deque([(3, 3, 6)])
# deque([(2, 3, 7), (3, 4, 7)])
# deque([(3, 4, 7), (1, 3, 8)])
# deque([(1, 3, 8), (3, 5, 8)])
# deque([(3, 5, 8), (1, 4, 9)])
# deque([(1, 4, 9), (2, 5, 9), (4, 5, 9)])
# deque([(2, 5, 9), (4, 5, 9), (1, 5, 10)])
# deque([(4, 5, 9), (1, 5, 10)])
# deque([(1, 5, 10), (5, 5, 10)])
# deque([(5, 5, 10)])