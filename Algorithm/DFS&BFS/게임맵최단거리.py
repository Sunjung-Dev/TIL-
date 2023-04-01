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

            if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]):
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
    answer = bfs(0, 0, maps)
    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))