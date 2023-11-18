from collections import deque

N = int(input())
visited = [[0 for col in range(N)] for row in range(N)]
ground = list()

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    cnt = 1

    while(queue):
        x, y = queue.popleft()
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= len(ground) or ny >= len(ground[0]):
                continue
            if ground[nx][ny] == '0':
                continue
            if ground[nx][ny] == '1' and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                cnt += 1
    return cnt 

ground = [list(input()) for _ in range(N)]

result = list()
for i in range(N):
    for j in range(N):
        if ground[i][j] == '1' and visited[i][j] == 0:
            result.append(bfs(i, j))

print(len(result))
for i in range(len(result)):
    print(result[i])
