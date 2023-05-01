from collections import deque

def bfs(x, y , maps):
    queue = deque()
    queue.append((x, y))
    checked_list = list()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    scale = 0
    while queue:
        x, y = queue.popleft()
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]):
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                scale += 1
                maps[nx][ny] = 0
                queue.append((nx, ny))
    return scale


def main():
    N, M = map(int, input().split())

    graph = []
    for i in range(N):
        graph.append(list(map(str, input())))

    print(graph)
    maps_w = [[0] * M for _ in range(N)]
    maps_b = [[0] * M for _ in range(N)]

    for i in range(0, len(graph)):
        for j in range(0, len(graph[i])):
            if graph[i][j] == 'W':
                maps_w[i][j] = 1
            elif graph[i][j] == 'B':
                maps_b[i][j] = 1

    score_w = 0
    score_b = 0

    for i in range(len(graph)):
        for j in range(0, len(graph)):
            if graph[i][j] == 'W':
                result_w = bfs(i, j, maps_w)
                score_w += (result_w * result_w)

    for i in range(len(graph)):
        for j in range(0, len(graph)):
            if graph[i][j] == 'B':
                result_b = bfs(i, j, maps_b)
                score_b+= (result_b * result_b)

    return score_w, score_b

print(main())
