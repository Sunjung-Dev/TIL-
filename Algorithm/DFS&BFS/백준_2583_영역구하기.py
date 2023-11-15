from collections import deque

N, M, K = map(int, input().split())
rectangle_list = list()
ground = [[0 for col in range(M)] for row in range(N)]

def bfs(x, y):
    cnt = 0 
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    queue = deque()
    queue.append((x, y))

    while(queue):
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= len(ground) or ny >= len(ground[0]):
                continue
            if ground[nx][ny] >= 1:
                continue
            if ground[nx][ny] == 0:
                ground[nx][ny] = 1
                queue.append((nx, ny))
                cnt += 1
    if cnt == 0 :
        cnt = 1
    return cnt

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    rectangle_list.append([[x1, y1], [x2, y2]])

for i in range(K):
    for j in range(rectangle_list[i][0][1], rectangle_list[i][1][1]):
        for k in range(rectangle_list[i][0][0], rectangle_list[i][1][0]):
            ground[j][k] += 1

result = list()

for i in range(N):
    for j in range(M):
        if ground[i][j] == 0:
           result.append(bfs(i, j))
result = sorted(result)
print(len(result))
for i in range(len(result)):
    print(result[i], end=' ')

            
            