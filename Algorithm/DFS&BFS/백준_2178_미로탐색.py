from collections import deque

N,M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

def bfs(x, y, graph):
    queue = deque()
    queue.append((x, y))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while(queue):
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= len(graph) or ny >= len(graph[0]):
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[-1][-1]

print(bfs(0, 0, graph))
