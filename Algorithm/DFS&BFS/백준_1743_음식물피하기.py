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
    N, M, K = map(int, input().split())

    graph = []
    for i in range(K):
        graph.append(list(map(int, input().split())))

    maps = [[0] * M for _ in range(N)]
    graph.sort()

    for i in range(0, len(graph)):
        maps[graph[i][0]-1][graph[i][1]-1] = 1 

    result_list = list()

    for i in range(len(graph)):
        result = bfs(graph[i][0], graph[i][1], maps)
        result_list.append(result)
    
    return max(result_list)

print(main())
